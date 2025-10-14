import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_freq, dynamic_range, verbose =False):
        self.gpio_pin = gpio_pin
        self.pwm_freq = pwm_freq
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_freq)
        duty=0
        self.pwm.start(duty)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, V):
        if not(0.0 <= V <= self.dynamic_range):
            print("Напряжение плохое")
            print("Устанавливаем нолик")
            V = 0
        duty=int(100*V/self.dynamic_range)
        self.pwm.ChangeDutyCycle(duty)

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.29, True)

        while True:
            try:
                voltage = float(input("Введите напряги: "))
                dac.set_voltage(voltage)
            except ValueError:
                print ("Не число \n")
        
    finally:
        dac.deinit()