import RPi.GPIO as GPIO
import time
inPINS = [17,27]
smoothingWindowLength=4

def getTimex():
    return time.time()

GPIO.setmode(GPIO.BCM)
GPIO.setup(inPINS, GPIO.IN)
upTimes = [[0] for i in range(len(inPINS))]
downTimes = [[0] for i in range(len(inPINS))]
deltaTimes = [[0] for i in range(len(inPINS))]

def my_callback1(channel):
  i = inPINS.index(channel)
  v = GPIO.input(inPINS[i])
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

try:
  while True:
    ovl = deltaTimes[0][-smoothingWindowLength:] # output first pin PWM
    ov = sorted(ovl)[len(ovl) // 2] #ov = np.mean(ovl)
    print("channel 1: " + str(ov))

    ovl = deltaTimes[1][-smoothingWindowLength:] # output first pin PWM
    ov = sorted(ovl)[len(ovl) // 2] #ov = np.mean(ovl)
    print("channel 2: " + str(ov))

    time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
