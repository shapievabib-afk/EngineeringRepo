import RPi.GPIO as GPIO
import time as TM
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN)
GPIO.setup(26, GPIO.OUT)
state = 0

while True:
    if GPIO.input(13):
        state = not state
        GPIO.output(26, state)
        TM.sleep(0.2)