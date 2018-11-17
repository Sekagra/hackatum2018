import threading
import time
import RPi.GPIO as GPIO

class Steering:
    def __init__(self, steering_pin):
        self.__steering_pin = steering_pin

        GPIO.setup(steering_pin, GPIO.OUT)
        self.__pwm = GPIO.PWM(steering_pin, 50) #50hz
        self.__pwm.start(6) #should be 50%

    def set_steering(self, steering):
        duty = 2 + steering / 100.0 * 8
        duty = max(min(duty, 10), 2) #bounds
        self.__pwm.ChangeDutyCycle(duty)
