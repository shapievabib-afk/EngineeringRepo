import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(6, GPIO.IN)
state = 1

while True:
    if GPIO.input(6):
        state = 1
        GPIO.output(26, state)
    else:
        GPIO.output(26, not state)
        
        