import RPi.GPIO as IO
import time
import mcp3021_driver as mcp #исполльзуем драйвер
import adc_plot as plt #это для графиков

adc = mcp.MCP3021(5.18)
time_values = [] #лист для времени
voltage_values = [] #лист для значений напряжение
duration = 3.0
try:
    start_time=time.time()
    now_time=time.time()
    while now_time-start_time<duration:
        now_time=time.time()
        voltage_values.append(adc.get_voltage())
        time_values.append(now_time-start_time)
    plt.plot_voltage_vs_time(time_values, voltage_values, 5.18)
    plt.plot_sampling_period_hist(time_values)
finally:
        adc.deinit() #да и в целом этот код многим похож на 2 задание. Не думаю
        #что мне нужны особые пометки.