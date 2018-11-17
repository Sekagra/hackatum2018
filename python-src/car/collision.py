import threading
import time
import RPi.GPIO as GPIO

# Dauer Trigger-Impuls
PULSE = 0.00001

# Anzahl Messwerte fuer Mittelwertbildung
BURST = 10

# Schallgeschwindigkeit/2
SPEED_2 = 17015

class Collision:
    def __init__(self, trigger_port, left_echo_port, right_echo_port, callback):
        self.__collision_thread = threading.Thread(
            target=self.loop, args=()
        )
        
        GPIO.setup([left_echo_port, right_echo_port], GPIO.IN)
        GPIO.setup(trigger_port, GPIO.OUT)
        GPIO.output(trigger_port, False)
        GPIO.add_event_detect(left_echo_port, GPIO.FALLING, callback=self.on_echo_received)
        GPIO.add_event_detect(right_echo_port, GPIO.FALLING, callback=self.on_echo_received)

        self.__trigger_port = trigger_port
        self.__left_echo_port = left_echo_port
        self.__right_echo_port = right_echo_port
        self.__callback = callback
        self.__in_flight = False

        print("Starting collision loop")
        self.__collision_thread.start()

    def on_echo_received(self, channel):
        if not self.__in_flight:
            return
        
        self.__in_flight = False
        delta = time.time() - self.__last_ping
        distance = delta * SPEED_2 - 10

        self.__callback(distance)

    def send_ping(self):
        if self.__in_flight:
            print("invalid call to send_ping - still in flight")
            return

        self.__in_flight = True

        GPIO.output(self.__trigger_port, True)
        time.sleep(PULSE)
        GPIO.output(self.__trigger_port, False) 

        self.__last_ping = time.time()

    def loop(self):
        while True:
            time.sleep(0.2) #timeout basically
            if self.__in_flight:
                self.__in_flight = False

            self.send_ping()
