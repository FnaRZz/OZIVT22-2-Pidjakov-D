# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
class Car: #Класс для представления автомобиля.
    def __init__(self, make, model): #Это метод инициализации с параметрами, обычно называют __init__
        self.make = make
        self.model = model  #Свойство класса для хранения марки автомобиля.
    def drive(self): # делаем первое действие (метод)
        print(f"Driving the {self.make} {self.model}")  # Эта строка выводит информацию о марке и модели автомобиля на экран.
my_car = Car("audi", "r8") #экземпляр класса Car
my_car.drive() # Для запуска первого действия
class ElectricCar(Car): #Новый класс который копирует все методы и атрибуты от класса Car.

    def __init__(self, make, model, battery_capacity): #функция с новыми параметрами
        super().__init__(make, model) #опять копируем класс с новыми параметрами
        self.battery_capacity = battery_capacity # из атрибута battery_capacity делаем экземпляр класса
    def charge(self): #делаем второе действие (метод)
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity}  kWh") #Вывод на экран
my_electric_car = ElectricCar("CyberTrack", "S", 50) #Создание экземпляра класса ElectricCar
my_electric_car.charge() # запуск второго действия
