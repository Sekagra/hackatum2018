import threading
import time
import RPi.GPIO as GPIO
import numpy as np

SMOOTHING_WINDOW = 5

class Receiver:
    def __init__(self, steering_port, callback):
        self.__receiver_thread = threading.Thread(
            target=self.loop, args=()
        )
        
        GPIO.setup(steering_port, GPIO.IN)
        GPIO.add_event_detect(steering_port, GPIO.BOTH, callback=self.trigger_callback)

        self.__steering_port = steering_port
        self.__callback = callback

        self.__upTimes = [0]
        self.__downTimes = [0]
        self.__deltaTimes = [0]

        print("Starting receiver loop")
        self.__receiver_thread.start()

    def trigger_callback(self, channel):
        if GPIO.input(self.__steering_port):
            self.__upTimes.append(time.time())
            if len(self.__upTimes) > SMOOTHING_WINDOW: 
                del self.__upTimes[0] # rotate buffer

            if len(self.__deltaTimes) > SMOOTHING_WINDOW:
                del self.__deltaTimes[0]  
        else:
            self.__downTimes.append(time.time())
            if len(self.__downTimes) > SMOOTHING_WINDOW:
                del self.__downTimes[0]      
        
            self.__deltaTimes.append(100 * (self.__downTimes[-2] - self.__upTimes[-2]) / (self.__upTimes[-1] - self.__upTimes[-2]))

    def loop(self):
        while True:
            values = self.__deltaTimes[-SMOOTHING_WINDOW:]
            print(values)
            average = np.mean(values)
            self.__callback((average - 6.5) / (13 - 6.5) * 100)
            time.sleep(0.1)
