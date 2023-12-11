# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
class Car: #Класс для представления автомобиля.
    def __init__(self, make, model): #Это метод инициализации с параметрами, обычно называют __init__
        self._make = make #защищенный атрибут
        self.__model = model  #Приватный атрибут

	def drive(self):
        print(f"Driving the {self._make} {self.__model}")

my_car = Car("audi", "r8") #экземпляр класса Car
print(my_car.__make)
my.car.drive()