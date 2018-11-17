import threading
import time
import RPi.GPIO as GPIO
import numpy as np

SMOOTHING_WINDOW = 5

class Receiver:
    def __init__(self, steering_port):
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
        if not GPIO.input(self.__steering_port):
            self.__downTimes.append(time.time())
            if len(self.__downTimes) > SMOOTHING_WINDOW:
                del self.__downTimes[0]
        else:
            self.__upTimes.append(time.time())
            if len(self.__upTimes) > SMOOTHING_WINDOW: 
                del self.__upTimes[0] # rotate buffer
        
        self.__deltaTimes.append((downTimes[-1] - upTimes[-2]) / (upTimes[-1] - downTimes[-1]))
        if len(self.__deltaTimes) > SMOOTHING_WINDOW:
            del self.__deltaTimes[0]

    def loop(self):
        while True:
            ovl = self.__deltaTimes[-SMOOTHING_WINDOW:] # output first pin PWM
            #ov = sorted(ovl)[len(ovl) // 2] 
            ov = np.mean(ovl)
            print("receiver: " + str(ov))
            time.sleep(0.1)
