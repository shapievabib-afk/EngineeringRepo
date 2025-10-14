import RPi.GPIO as GPIO
class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        return [int(element) for element in bin(number)[2:].zfill(8)]

    def set_voltage(self, V):
        if not (0.0<= V <= self.dynamic_range):
            print("Напряжение недопустимо, иди гуляй")
            print("Устанавливаем напряжение 0.0 В")
            V = 0.0
        nV = int(255*V/self.dynamic_range)
        v_ar = self.set_number(nV)
        for i in self.gpio_bits:
            GPIO.output(i, v_ar[self.gpio_bits.index(i)])

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16,20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")


    finally:
        dac.deinit()

