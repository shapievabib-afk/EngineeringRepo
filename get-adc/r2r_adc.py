import RPi.GPIO as GPIO
import time as GOIDA

class R2R_ADC:
    def __init__(self, dynamic_range = 3.3, compare_time = 0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        self.voltage = 0.0
        self.max_dac_value = 0.0
        self.value = 0

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def dec2bin(value):
        return [int(element) for element in bin(value)[2:].zfill(8)]

    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio, number)
        #может стоить просто применить что-то вроде self.number = number как в r2r_dac но добавить выход для ацп

    #абсолютно безосновательно попробуем добавить функцию вольтажа. Ибо мы в намбер должны же хоть что-то возвращать ало
    #def crazy_voltage(voltage):
     #   self.voltage = int(bin(value))

    def sequential_counting_adc(self): ## Данная реализация нуждает в проверке, сделано на веру хехе
        max_dac_number = (1<<self.dac.bits) - 1

        for value in range (R2R_ADC.max_dac_value + 1):
            self.dac.set_value(value)

            GOIDA.compare_time = R2R_ADC.compare_time
            bits_gpio_output = self.bits_gpio.read()

            if bits_gpio_output == 1:
                return value
            
        return max_dac_number

    def get_sc_voltage(self):
        self.number = int(R2R_ADC.value)

        return self.number

if __name__ == "__main__":
    try:
        dac = R2R_ADC(R2R_ADC.bits_gpio, 3.183, 0.01, True)

        while True:
            try:
                R2R_ADC.sequential_counting_adc
                print(f"Значение: {R2R_ADC.self.number}")
                

            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")

    finally:
        dac.deinit()
