#! /usr/bin/env python3

import RPi.GPIO as GPIO
import time

from stepper import Stepper
from stepper2 import Engine

inPINS = [2,3,4,14,15,18,17,27,22,23]
smoothingWindowLength=4

upTimes = [[0] for i in range(len(inPINS))]
downTimes = [[0] for i in range(len(inPINS))]
deltaTimes = [[0] for i in range(len(inPINS))]

def getTimex():
        return time.time()

def my_callback1(channel):
    i = inPINS.index(channel)
    v = GPIO.input(inPINS[i])
    
    #GPIO.output(outPINS[0], v) # mirror input state to output state directly (forward servo value only) - don't set PWM then for this pin
    if (v==0):
        downTimes[i].append(getTimex())
        if len(downTimes[i])>smoothingWindowLength: del downTimes[i][0]
    else:
        upTimes[i].append(getTimex())
        if len(upTimes[i])>smoothingWindowLength: del upTimes[i][0]
    deltaTimes[i].append( (downTimes[i][-1]-upTimes[i][-2])/(upTimes[i][-1]-downTimes[i][-1]) )
    if len(deltaTimes[i])>smoothingWindowLength: del deltaTimes[i][0]

    GPIO.add_event_detect(inPINS[0], GPIO.BOTH, callback=my_callback1)
    GPIO.add_event_detect(inPINS[1], GPIO.BOTH, callback=my_callback1)

def test_recv():
    GPIO.setup(inPINS, GPIO.IN)
    
    try:
        while True:
            ovl = deltaTimes[0][-smoothingWindowLength:] # output first pin PWM
            ov = sorted(ovl)[len(ovl) // 2] #ov = np.mean(ovl)
            print(ov)
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()

def test_servo():
    print("Testing servo")
    servoPIN = 13
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)
    p.start(2.5)

    p.ChangeDutyCycle(2)
    time.sleep(2)
    p.ChangeDutyCycle(10)
    time.sleep(2)

    for i in range(100):
        p.ChangeDutyCycle(2 + i/100.0 * 8)
        time.sleep(.2)

def test():
    testPIN = 13
    print("Testing ping %d" % testPIN)
    GPIO.setup(testPIN, GPIO.OUT)
    GPIO.output(testPIN, GPIO.HIGH)
    time.sleep(10)

def test_stepper():
    A=18
    B=23
    C=24
    D=25

    stepper = Stepper(A, B, C, D)
    stepper.do_full_turn()
    time.sleep(1)

def test_stepper2():
    cfg = {
        "PIN_NOT_ENABLE" : 19,
        "PIN_DIR" : 13,
        "PIN_MS1" : 17,
        "PIN_MS2" : 27,
        "PIN_MS3" : 22,
        "PIN_STEP" : 26
    }

    stepper = Engine(cfg)
    for i in range(11):
        print("%d%%" % (i * 10))
        stepper.drive(i * 10)
        time.sleep(2)
    stepper.drive(0)
    time.sleep(2)

def main():
    print("In main")
    GPIO.setmode(GPIO.BCM)
    #test_servo()
    #test()
    #test_stepper()
    test_stepper2()
    GPIO.cleanup()


if __name__ == "__main__":
    main()
    

