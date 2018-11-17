from time import sleep
import time
import RPi.GPIO as GPIO

class Stepper():
    def __init__(self, A, B, C, D):
        self.__A = A
        self.__B = B
        self.__C = C
        self.__D = D

        self.__delay = 0.0007
        self.__init_pins()

    def __init_pins(self):
        GPIO.setup(self.__A, GPIO.OUT)
        GPIO.setup(self.__B, GPIO.OUT)
        GPIO.setup(self.__C, GPIO.OUT)
        GPIO.setup(self.__D, GPIO.OUT)
        GPIO.output(self.__A, GPIO.LOW)
        GPIO.output(self.__B, GPIO.LOW)
        GPIO.output(self.__C, GPIO.LOW)
        GPIO.output(self.__D, GPIO.LOW)

    def __pos_1(self):
        GPIO.output(self.__D, GPIO.HIGH)
        sleep(self.__delay)
        GPIO.output(self.__D, GPIO.LOW)

    def __pos_2(self):
        GPIO.output(self.__C, GPIO.HIGH)
        GPIO.output(self.__D, GPIO.HIGH)
        sleep(self.__delay)
        GPIO.output(self.__C, GPIO.LOW)
        GPIO.output(self.__D, GPIO.LOW)

    def __pos_3(self):
        GPIO.output(self.__C, GPIO.HIGH)
        sleep(self.__delay)
        GPIO.output(self.__C, GPIO.LOW)

    def __pos_4(self):
        GPIO.output(self.__B, GPIO.HIGH)
        GPIO.output(self.__C, GPIO.HIGH)
        sleep(self.__delay)
        GPIO.output(self.__B, GPIO.LOW)
        GPIO.output(self.__C, GPIO.LOW)

    def __pos_5(self):
        GPIO.output(self.__B, GPIO.HIGH)
        sleep(self.__delay)
        GPIO.output(self.__B, GPIO.LOW)

    def __pos_6(self):
        GPIO.output(self.__A, GPIO.HIGH)
        GPIO.output(self.__B, GPIO.HIGH)
        sleep(self.__delay)
        GPIO.output(self.__A, GPIO.LOW)
        GPIO.output(self.__B, GPIO.LOW)

    def __pos_7(self):
        GPIO.output(self.__A, GPIO.HIGH)
        sleep(self.__delay)
        GPIO.output(self.__A, GPIO.LOW)

    def __pos_8(self):
        GPIO.output(self.__D, GPIO.HIGH)
        GPIO.output(self.__A, GPIO.HIGH)
        sleep(self.__delay)
        GPIO.output(self.__D, GPIO.LOW)
        GPIO.output(self.__A, GPIO.LOW)

    def do_full_turn(self):
        t = time.time()
        for _ in range(40):
            print(self.__delay)
            for _ in range (256):
                self.__pos_1()
                self.__pos_2()
                self.__pos_3()
                self.__pos_4()
                self.__pos_5()
                self.__pos_6()
                self.__pos_7()
                self.__pos_8()
            self.__delay -= 0.00005
        print(time.time() - t)