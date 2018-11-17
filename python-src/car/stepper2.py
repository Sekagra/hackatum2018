import time
import RPi.GPIO as GPIO
import threading

#not_en_pin = 19
#dir_pin = 13
#ms1_pin = 17
#ms2_pin = 27
#ms3_pin = 22
#step_pin = 26

ANGLE = 1.8
FULL_SPEED_DELAY = 0.0008
ONE_PERCENT_SPEED_DELAY = 0.01
class Engine:
    def __init__(self, cfg):
        self.__not_en_pin = cfg["PIN_NOT_ENABLE"]
        self.__dir_pin = cfg["PIN_DIR"]
        self.__ms1_pin = cfg["PIN_MS1"]
        self.__ms2_pin = cfg["PIN_MS2"]
        self.__ms3_pin = cfg["PIN_MS3"]
        self.__step_pin = cfg["PIN_STEP"]

        self.__init()

        self.disable()

        self.__drive_thread = None
        self.__driving = False

    def __init(self):
        GPIO.setup(self.__not_en_pin, GPIO.OUT)
        GPIO.output(self.__not_en_pin, GPIO.LOW)

        GPIO.setup(self.__dir_pin, GPIO.OUT)
        GPIO.output(self.__dir_pin, GPIO.LOW)

        GPIO.setup(self.__ms1_pin, GPIO.OUT)
        GPIO.output(self.__ms1_pin, GPIO.LOW)

        GPIO.setup(self.__ms2_pin, GPIO.OUT)
        GPIO.output(self.__ms2_pin, GPIO.LOW)

        GPIO.setup(self.__ms3_pin, GPIO.OUT)
        GPIO.output(self.__ms3_pin, GPIO.LOW)

        GPIO.setup(self.__step_pin, GPIO.OUT)
        GPIO.output(self.__step_pin, GPIO.LOW)

    def disable(self):
        GPIO.output(self.__not_en_pin, GPIO.HIGH)

    def enable(self):
        GPIO.output(self.__not_en_pin, GPIO.LOW)

    def __step(self, delay):
        GPIO.output(self.__step_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(self.__step_pin, GPIO.LOW)

    def __drive_loop(self):
        while self.__driving:
            # Full step mode
            for _ in range(int(360/ANGLE)):
                self.__step(
                    FULL_SPEED_DELAY +
                    (100 - self.__speed) * (ONE_PERCENT_SPEED_DELAY - FULL_SPEED_DELAY) / 99
                )
        self.__drive_thread = None

    def drive(self, speed):
        if speed < 0:
            self.drive(0)
            return
        elif speed == 0:
            self.__driving = False
            return
        self.__speed = speed
        self.enable()
        if not self.__drive_thread:
            self.__drive_thread = threading.Thread(target=self.__drive_loop, args=())
            self.__driving = True
            self.__drive_thread.start()
