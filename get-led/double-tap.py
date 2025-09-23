import RPi.GPIO as GPIO
import time

leds= [16, 12, 25, 17, 27, 23, 22, 24]
up = 9
down = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2
final_sleep_time = 2

while True:
    if GPIO.input(up):
        
        num = num+1
        if num>8:
            num = 0
            print(num, dec2bin(num))
            time.sleep(sleep_time)
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(down):
        num = num -1
        print(num, dec2bin(num))
        time.sleep(sleep_time)


    if GPIO.input(up) and GPIO.input(down):
        num=255
        print(num, dec2bin(num))
        time.sleep(final_sleep_time)

    GPIO.output(leds, dec2bin(num))
