import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
leds= [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

dynamic_range = 3.3

def voltage_to_number(voltage):
    if not (0.0<= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический ЦАП (0.0 - {dynamic_range: .2f} В)")
        print("Устанавливаем 0.0 В")
        return 0

    return int(voltage / dynamic_range *255)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def number_to_dac(number):
    GPIO.output(leds, dec2bin(number))

try:
     while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
            print(dec2bin(number))

        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()