from car.stepper2 import Engine
from car.collision import Collision
from udp_server.server import Server

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
        ip = "131.159.198.40"
        port = 5001
        self.__udp_server = Server(ip, port, self.callback_function)
        GPIO.setmode(GPIO.BCM)
        self.__engine = Engine(pin_cfg)
        self.__collision = Collision(16, 20, 21, self.distance_callback)

    def distance_callback(self, distance):
        print("got distance:" + str(distance))
        if distance < 10:
            raise Exception("Kabumm")

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
