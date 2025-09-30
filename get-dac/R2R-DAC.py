import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
bits = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
dynamic_range = 3.3

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio.gpio_bitsself.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    set_number(self, number):
        self.number = number
        print(f"Число на входе в ЦАП: {self.number")

    set_voltage(self, voltage):
        self.voltage = voltage

if __name__ == "__main__":
    try:
        dac = R2R_DAC(bits, 3.183, True)

        while True:
            try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            
            dec.set_voltage(voltage)
            print(dec2bin(number))

        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")

    finally:
        dac.deinit()
        