import time
import pwm_dac as pwm
import signal_generator as sig

amplitude = 3
sig_freq = 5
sampl_freq = 250

try:
    dc = pwm.PWM_DAC(12, 1000, 3.29, True)

    while True:
        try:
            fx=sig.get_sin_wave_amplitude(sig_freq, time.time())
            dc.set_voltage(fx*amplitude)
            sig.wait_for_sampling_period(sampl_freq)
        except ValueError:
            print("Не число!\n")

finally:
    dc.deinit()