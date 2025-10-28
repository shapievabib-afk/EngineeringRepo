import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
import adc_plot as plot

class R2R_ADC:
    def __init__(self, voltage, timer):
        self.voltage = voltage
        self.timer = timer

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

voltage_values = [R2R_ADC(voltage) for voltage in []]
time_values = [R2R_ADC(timer) for timer in []]
duration = 0.3

if __name__ == '__main__':

    adc = R2R_ADC()


    try:
        start = 0
        time.start = start
        while (start<100):
            voltage_values[start] = R2R_ADC.voltage
            time_values[start] = R2R_ADC.timer
            start+=1

        max_voltage=voltage_values[99]
        plot.plt_voltage_vs_time(time_values, voltage_values, max_voltage)



    finally:
            adc.deinit()
        
        #need to fix


