import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
bits = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(bits, GPIO.OUT)
GPIO.output(bits, 0)
dynamic_range = 3.3

class PWM_DAC:
    def __init__(self, pwm_pin, pwm_frequency, dynamic_range, verbose=False):
        self.pwm_pin = pwm_pin
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.pwm_frequency = pwm_frequency
        self.pwm = None
        
        # Настраиваем ШИМ на указанном пине
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, self.pwm_frequency)
        self.pwm.start(0)  # Запускаем ШИМ с 0% заполнения
        
        if self.verbose:
            print(f"PWM DAC инициализирован на пине {pwm_pin}, частота {pwm_frequency} Гц")

    def deinit(self):
        if self.pwm:
            self.pwm.stop()
        GPIO.cleanup()

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print("Напряжение недопустимо")
            voltage = max(0, min(voltage, self.dynamic_range))
        
        # Конвертируем напряжение в коэффициент заполнения ШИМ (0-100%)
        duty_cycle = (voltage / self.dynamic_range) * 100
        self.pwm.ChangeDutyCycle(duty_cycle)
        
        if self.verbose:
            print(f"Установлено напряжение: {voltage:.2f} В, коэффициент заполнения: {duty_cycle:.1f}%")

def dec2bin(number):
    return [int(bit) for bit in bin(number)[2:].zfill(8)]

if __name__ == "__main__":
    try:
        # Используем один из пинов из списка bits для ШИМ
        dac = PWM_DAC(pwm_pin=21, pwm_frequency=500, dynamic_range=3.3, verbose=True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах (0-3.3): "))
                dac.set_voltage(voltage)
                
                # Для параллельного ЦАП (если хотите использовать оба варианта)
                number = int((voltage / 3.3) * 255)
                binary_number = dec2bin(number)
                GPIO.output(bits, binary_number)
                print(f"Двоичный код для параллельного ЦАП: {binary_number}")
                
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
            except KeyboardInterrupt:
                print("\nВыход из программы")
                break

    finally:
        dac.deinit()
