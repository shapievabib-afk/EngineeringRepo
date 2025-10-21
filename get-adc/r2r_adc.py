import RPi.GPIO as GPIO
import time as GOIDA

class R2R_ADC:
    def __init__(self, dynamic_range = 3.3, compare_time = 0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        self.voltage = 0.0
        self.max_dac_value = 255
        self.value = 0
        self.max_dac_number = 0
        

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def dec2bin(self, value):
        return [int(element) for element in bin(value)[2:].zfill(8)]

    def number_to_dac(self, number):
        #binary_value = self.dec2bin(number)
        GPIO.output(self.bits_gpio, number)
        #может стоить просто применить что-то вроде self.number = number как в r2r_dac но добавить выход для ацп

    #абсолютно безосновательно попробуем добавить функцию вольтажа. Ибо мы в намбер должны же хоть что-то возвращать ало
    #def crazy_voltage(voltage):
     #   self.voltage = int(bin(value))

    def sequential_counting_adc(self): ## Данная реализация нуждает в проверке, сделано на веру хехе
        self.max_dac_number = self.max_dac_value

        for value in range (self.max_dac_number + 1):
            self.number_to_dac(value)
            GOIDA.sleep(self.compare_time)
            comparator_output = GPIO.input(self.comp_gpio)

            if self.verbose:
                print(f"Значение: {value}, Comparator: {comparator_output}")

            if comparator_output == 1:
                self.value = value
                return value

        self.value = self.max_dac_number
        return self.max_dac_number

    def get_sc_voltage(self):
        voltage = (self.value / self.max_dac_value) * self.dynamic_range
        return voltage

if __name__ == "__main__":
    try:
        adc = R2R_ADC()

        while True:
            try:
                value = adc.sequential_counting_adc()
                voltage = adc.get_sc_voltage()
                print(f"Значение: {value}")
                print(f"Напряжение: {voltage:.2f} В")

                GOIDA.sleep(0.5)
            except ValueError:
                print("ОШИБКААААААААААААААААА")
                break

    finally:
        adc.deinit()
