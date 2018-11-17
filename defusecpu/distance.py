import RPi.GPIO as GPIO
import time
import datetime

# GPIOs fuer den US-Sensor
TRIG = 5
ECHO = 6

# Dauer Trigger-Impuls
PULSE = 0.00001

# Anzahl Messwerte fuer Mittelwertbildung
BURST = 10

# Schallgeschwindigkeit/2
SPEED_2 = 17015

# BCM GPIO-Referenen verwenden (anstelle der Pin-Nummern)
# und GPIO-Eingang definieren
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.remove_event_detect(ECHO)
GPIO.output(TRIG, False)
time.sleep(1)                   # Setup-Zeit fuer Sensor

stopp = 0                       # Variableninit
start = 0
distance = 0

def pulse():                    # Funktion zum Starten der Messung
  global start
  global stopp
  global distance

  GPIO.output(TRIG, True)       # Triggerimpuls  erzeugen
  time.sleep(PULSE)
  GPIO.output(TRIG, False)
  stopp = 0                     # Werte auf 0 setzen
  start = 0
  distance = 0                  # und Event starten


def measure(x):                 # Callback-Funktion fuer ECHO
  global start
  global stopp
  global distance
  if GPIO.input(ECHO):          # steigende Flanke, Startzeit speichern
    start = time.time()
  else:                         # fallende Flanke, Endezeit speichern
    stopp = time.time()
    delta = stopp - start       # Zeitdifferenz und Entfernung berechnen
    distance = delta * SPEED_2


def measure_range():            # Bildet Mittelwert von BURST Messungen
  values = []
  sum = 0
  for i in range(0, BURST):
    pulse()                     # Messung starten
    time.sleep(0.040)           # Warten, bis Messung zuende
    if distance == 0:
        continue
    values.append(distance)     # Wert im Array speichern und aufsummieren
    sum = sum + distance
    print("Messwert: %1.1f" % distance) # Kontrollausgabe
    time.sleep(0.060)
  return sum/len(values);             # Mittelwert zurueckgeben

# do it
try:
  GPIO.add_event_detect(ECHO, GPIO.BOTH, callback=measure)
  while True:
    Dist = measure_range()
    print("Range = %1.1f cm" % Dist)
#    time.sleep(1)

# reset GPIO settings if user pressed Ctrl+C
except KeyboardInterrupt:
  print("Bye!")
  GPIO.cleanup()
