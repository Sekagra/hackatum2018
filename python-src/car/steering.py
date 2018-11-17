import threading
import time
import RPi.GPIO as GPIO

class Steering:
    def __init__(self, steering_pin):
        self.__steering_pin = steering_pin

        GPIO.setup(steering_pin, GPIO.OUT)
        self.__pwm = GPIO.PWM(steering_pin, 50) #50hz
        self.__pwm.start(6.5) #should be 50%

    def set_steering(self, steering):
        duty = 4 + steering / 100.0 * 5
        duty = max(min(duty, 9), 4) #bounds
        print("duty: " + str(duty))
        self.__pwm.ChangeDutyCycle(duty)
