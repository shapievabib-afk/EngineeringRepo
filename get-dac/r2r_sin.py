import time
import signal_generator as signal
import r2r_dac_modified as r2r

amplitude = 3
frequency = 10
sampl_freq = 1000


try:
    
    dc = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.2, True)


    while True:
        try:
            fx = signal.get_triangle_wave_amplitude(frequency, time.time())
            dc.set_voltage(fx*amplitude)
            signal.wait_for_sampling_period(sampl_freq)
        except ValueError:
            print("Не число!\n")

finally:
    dc.deinit()