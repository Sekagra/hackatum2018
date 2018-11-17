from car.stepper2 import Engine
from car.collision import Collision
from car.receiver import Receiver
from car.steering import Steering
from udp_server.server import Server
from udp_server.server import Client

import RPi.GPIO as GPIO
import json

pin_cfg = {
    "PIN_NOT_ENABLE" : 19,
    "PIN_DIR" : 13,
    "PIN_MS1" : 17,
    "PIN_MS2" : 27,
    "PIN_MS3" : 22,
    "PIN_STEP" : 26
}

class Runner:
    def __init__(self):
        #server_ip = "192.168.2.1"
        server_ip = "131.159.198.40"
        server_port = 5001
        client_ip = "192.168.2.72"
        client_port = 5003
        self.__udp_server = Server(server_ip, server_port, self.callback_function)
        self.__client = Client(client_ip, client_port)
        GPIO.setmode(GPIO.BCM)
        self.__engine = Engine(pin_cfg)
        self.__steering = Steering(23)
        self.__collision = Collision(16, 20, 21, self.distance_callback)
        self.__receiver = Receiver(12, self.receiver_callback)

    def distance_callback(self, distance):
        print("got distance:" + str(distance))
        if distance < 10:
            # send "hit the wall" to app
            self.__client.send_data("explode")

    def receiver_callback(self, rotation):
        print("steering rotation " + str(rotation))
        self.__steering.set_steering(rotation)

    def callback_function(self, message):
        print(message)
        parsed_msg = json.loads(message)

        if parsed_msg["cmd"] == "start":
            speed = int(parsed_msg["speed"])
            self.__engine.drive(speed)
        elif parsed_msg["cmd"] == "lose":
            self.__engine.drive(0)

if __name__ == "__main__":
    r = Runner()
