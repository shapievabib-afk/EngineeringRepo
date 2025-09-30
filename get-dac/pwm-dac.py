import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
bits = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(bits, GPIO.OUT)
GPIO.output(bits, 0)
dynamic_range = 3.3

class PWM_DAC:
    def __init__(self, gpio_bits, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.number = 0 
        self.voltage = 0 
        self.pwm_frequency = 500

        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        self.number = number
        print(f"Число на входе в ЦАП: {self.number}")

    def set_voltage(self, voltage):
        self.voltage = voltage

    def dec2bin(number):
        return [int(bit) for bit in bin(number)[2:].zfill(8)]

def voltage_to_number(voltage):
        if not (0.0<= voltage <= dynamic_range):
            print("Напряжение недопустимо, иди гуляй")
            print("Устанавливаем напряжение 0.0 В")
            voltage = 0.0
            return 0

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                print(f"Коэффициент заполнения: 500")

                if not (0.0<= voltage <= dynamic_range):
                    print("Напряжение недопустимо, иди гуляй")
                    print("Устанавливаем напряжение 0.0 В")
                    voltage = 0.0
                    number = 0
                
                else:
                    number = int((voltage/3.183) *255)
                

                dac.set_voltage(voltage)
                #number = int((voltage/3.183) *255)
                #dac.set_number(number)
                #binary_number = PWM_DAC.dec2bin(number)
                #GPIO.output(bits, binary_number)
                print(PWM_DAC.dec2bin(number))

            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")

    finally:
        dac.deinit()