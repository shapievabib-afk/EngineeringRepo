import smbus

class TW_BITS:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)
        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")
            return

        if not (0<= number <= 4095):
            print("Число выходит за рязрядность MCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >>8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

    def set_voltage(self, voltage):
            if not (0.0 <= voltage <= self.dynamic_range):
                print("Напряжение недопустимо")
                voltage = max(0, min(voltage, self.dynamic_range))
            number = int((voltage / self.dynamic_range) * 4095)
            self.set_number(number)

if __name__ == "__main__":
    try:
        dac = TW_BITS(dynamic_range=5, address = 0x61, verbose=True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах (0-3.3): "))
                dac.set_voltage(voltage)
                
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
            except KeyboardInterrupt:
                print("\nВыход из программы")
                break

    finally:
        dac.deinit()