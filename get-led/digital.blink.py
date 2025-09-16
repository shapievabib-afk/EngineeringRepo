import RPi.GPIO as gpio
import time as TM

gpio.setmode(gpio.BCM)
gpio.setup(26, gpio.OUT)
state=0
period=0.3

while True:
    gpio.output(26, state)
    state= not state
    TM.sleep(period)