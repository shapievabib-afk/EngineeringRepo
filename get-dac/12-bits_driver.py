import smbus

class TW_BITS:
    def __init__(self, dynamic_range, adress=0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.adress = adress
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")

        if not (0<= number <= 4095):
            print("Число выходит за рязрядность MCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >>8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address <<1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")

    def set_voltage(self, voltage):
            if not (0.0 <= voltage <= self.dynamic_range):
                print("Напряжение недопустимо")
                voltage = max(0, min(voltage, self.dynamic_range))

if __name__ == "__main__":
    try:
        dac = TW_BITS(dynamic_range=3.3, adress = 0x61, verbose=True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах (0-3.3): "))
                dac.set_voltage(voltage)
                
                number = int((voltage / 3.3) * 255)
                
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
            except KeyboardInterrupt:
                print("\nВыход из программы")
                break

    finally:
        dac.deinit()