
import time
import adc_plot as plot
import r2r_adc

adc = r2r_adc.R2R_ADC(3.29, 0.0001)
voltage_values = []
time_values = []
duration = 3.0

try:
    start = time.time()
    now = time.time()
    counter = 0
    while now-start<=duration:
            
        now = time.time()
        voltage_values.append(adc.get_sc_voltage())
        time_values.append(now- start)

    plot.plt_voltage_vs_time(time_values, voltage_values, 3.3)



finally:
        adc.deinit()
        
        #need to fix... still



