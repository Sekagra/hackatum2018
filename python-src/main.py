from car.stepper2 import Engine
from udp_server.server import Server

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
        ip = "192.168.2.1"
        port = 5003
        self.__udp_server = Server(ip, port, self.callback_function)
        self.__engine = Engine(pin_cfg)

    def callback_function(self, message):
        print(message)
        parsed_msg = json.loads(message)

        if parsed_msg["cmd"] == "start":
            speed = int(parsed_msg["speed"])
            self.__engine.drive(speed)
    