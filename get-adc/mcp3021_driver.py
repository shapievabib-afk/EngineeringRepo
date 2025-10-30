import smbus as I2C
import time
class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = I2C.SMBus(1)
        self.verbose = verbose
        self.dynamic_range = dynamic_range
        self.address = 0x4D #Инит делает важную часть кода, тут: подключение к шине I2C. Включение вывода(vewrbose)
        #Максимальное измерение задается через dynamic range

    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0) #чтение слова гыгы
        lower_data_byte = data >> 8 #сдвиг слова на 8 битов
        upper_data_byte = data & 0xFF #Используем маску, оставляем младший бит(что бы это ни значило)
        number = (upper_data_byte << 6) | (lower_data_byte >> 2) #Берем старший байт данных и сдвигаем на 6 бит влево, а младший байт сдвигаем на 2 вправо
        if self.verbose:
            print(f"Принятые данные {data}, старший бит {upper_data_byte}, младший бит {lower_data_byte}, число {number}")
        return number
        
    def get_voltage(self):
        return self.get_number()/1023*self.dynamic_range #функция, которая возвращает нам число заместо вольтажа. Эдакий трейд ин циферками.
    #Пометка для себя- 1023 это предельное значение, которое вообще может выдать 10-битный АЦП(А у нас какой?). 8ми битный вроде может выдать вообще максимум 256(0 и 255)

if (__name__ == "__main__"):
    try:
        adc=MCP3021(5.18) #создали объект АЦП и установили максимальный вольтаж
        while True: #Бесконечностей цикл
            V=adc.get_voltage() #в эту переменную мы заносим напряжение, которое потом выводим.
            print(V)
            time.sleep(1)
            
    finally:
        adc.deinit()#чтобы пахало как надо, надо за собой убирать