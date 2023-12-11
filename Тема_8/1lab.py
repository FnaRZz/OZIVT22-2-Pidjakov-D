# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
class Car: #Класс для представления автомобиля.
    def __init__(self, make, model): #Это метод инициализации с параметрами, обычно называют __init__
        self.make = make
        self.model = model  #Свойство класса для хранения марки автомобиля.

my_car = Car("audi", "r8") #экземпляр класса Car