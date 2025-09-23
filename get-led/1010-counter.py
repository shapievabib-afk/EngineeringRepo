import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
leds= [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
GPIO.input(9, GPIO.IN)
GPIO.input(10, GPIO.IN)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

if GPIO.input(up):
    num = num + 1
    print(num, dec2bin(num))
    time.sleep(sleep_time)

else GPIO.input(down):
    num = num + 1
    print(num, dec2bin(num))
    time.sleep(sleep_time)