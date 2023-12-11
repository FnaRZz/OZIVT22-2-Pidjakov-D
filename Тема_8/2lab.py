# для вывода текущего времени
import datetime
r = datetime.datetime.now()
print (r)

# основной код
class Car: #Класс для представления автомобиля.
    def __init__(self, make, model): #Это метод инициализации с параметрами, обычно называют __init__
        self._make = make
        self.__model = model  #Свойство класса для хранения марки автомобиля.
    def drive(self): # делаем первое действие (метод)
        print(f"Driving the {self._make} {self.__model}")  # вывод на экран

my_car = Car("audi", "r8") #экземпляр класса Car
print(my_car._make)
#print(my_car.__model)
my_car.drive()