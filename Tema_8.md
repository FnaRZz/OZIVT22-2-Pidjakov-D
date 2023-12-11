# Тема 8. Основы объектно-ориентированного программирования
Отчет по Теме #8 выполнил(а):
- Деревянкин Владислав Владимирович
- ОЗИВТ(ППК)-22-2-у

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | - | - |
| Задание 7 | - | - |
| Задание 8 | - | - |
| Задание 9 | - | - |
| Задание 10 | - | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car: #Класс для представления автомобиля.
    def __init__(self, make, model): #Это метод инициализации с параметрами, обычно называют __init__
        self.make = make
        self.model = model  #Свойство класса для хранения марки автомобиля.

my_car = Car("audi", "r8") #экземпляр класса Car
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/4fe60656-083d-448b-9446-e26be0acb6c1)


## Выводы
Создали класс с методом и его экземпляром.

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car: #Класс для представления автомобиля.
    def __init__(self, make, model): #Это метод инициализации с параметрами, обычно называют __init__
        self.make = make
        self.model = model  #Свойство класса для хранения марки автомобиля.

    def drive(self): # Метод для управления автомобилем
        print(self.make,self.model) # Вывод информации о марке и модели
        print ('едет')

my_car = Car("audi", "r8") #экземпляр класса Car
my_car.drive() # Для запуска
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/d7634aba-9638-49bb-a9c8-a76600dcc9b1)
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/a4cdcd03-6348-4cff-9675-297a0cbe7041)


## Выводы
Добавили код из первого задания и дополнили его дополнительным атрибутом и методом класса


## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Михаил А. Панов Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль

```python
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
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/18c4db07-b538-49aa-a91e-669ee14784fb)

## Выводы

Сделали второй метод с добавочным действием.


## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
class Car: #Класс для представления автомобиля.
    def __init__(self, make, model): #Это метод инициализации с параметрами, обычно называют __init__
        self._make = make
        self.__model = model  #Свойство класса для хранения марки автомобиля.
    def drive(self): # делаем первое действие (метод)
        print(f"Driving the {self._make} {self.__model}")  # вывод на экран.

my_car = Car("audi", "r8") #экземпляр класса Car
print(my_car._make)
#print(my_car.__model)
my_car.drive()
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/7a12f903-e57c-48e4-837c-a1fa2ed6c6b9)


## Выводы

Сделали защищенный атрибут производителя и приватный атрибут модели.

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Shape: #Создаем новый класс
    def area(self): #создаем затычку для того чтобы в конце её использовать
        pass #скипаем
class Rectangle(Shape): #Создаем новый класс
    def __init__(self, width, height): #Делаем функцию (метод) с параметрами длины и ширины
        self.width = width # атрибутыч длины
        self.height = height #атрибут ширины

    def area(self): # теперь используем затычку и возвращаем результат на area
        return self.width * self.height #

class Circle(Shape): #новый класс
    def __init__(self, radius): #Делаем функцию (метод) с параметром радиуса
        self.radius = radius #атрибут радиуса прописываем обязательно

    def area(self): #опять используем затычку чтобы через неё выводить ответ
        return 3.14 * self.radius * self.radius #вычисления

shapes = [Rectangle(4, 5), Circle(3)] #теперь заводим данные в них через список
for shape in shapes: #делаем цикл чтобы пройтись по каждому классу
    print(shape.area()) #выводим ответ в консоль
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/70ff8ec2-5e80-4551-bb9f-63e977b3357a)

## Выводы

Сделали с помощью классов подсчёт площади фигуры

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class vn:
    def __init__(self, Name,janr,score,prodoljitelnost):
        self.Name = Name
        self.janr = janr
        self.score = score
        self.prodoljitelnost = prodoljitelnost

    def print_s (self):
        print(f"game {self.Name} {self.janr} {self.score} {self.prodoljitelnost}")  # просто нужен для вывода

vndb = vn('Everlasting Summer','eroge','7.16','25hr')
vndb.print_s() # Для запуска первого действия
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/bd313674-ed0f-4947-b350-4927696b455a)


Сделали свой класс, атрибутами с выводом результата

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class vn:
    def __init__(self, Name,janr,score,prodoljitelnost):
        self.Name = Name
        self.janr = janr
        self.score = score
        self.prodoljitelnost = prodoljitelnost

    def print_s (self):
        print(f"game {self.Name} {self.janr} {self.score} {self.prodoljitelnost}")  # просто нужен для вывода

vndb = vn('Everlasting Summer','eroge','7.16','25hr')
vndb.print_s() # Для запуска первого действия
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/bd313674-ed0f-4947-b350-4927696b455a)

## Выводы

Тоже самое сделал как и в прошлом. 
  
## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Everlasting_Summer:
    def __init__(self,janr,score,prodoljitelnost):
        self.janr = janr
        self.score = score
        self.prodoljitelnost = prodoljitelnost

    def print_s (self):
        print(f"game {self.janr} {self.score} {self.prodoljitelnost}")  # просто нужен для вывода
ruvn = Everlasting_Summer('eroge','7.16','25hr')
ruvn.print_s() # Для запуска первого действия
class vn(Everlasting_Summer):
    def __init__(self,janr, score, prodoljitelnost,name):
        super().__init__(janr,score,prodoljitelnost)
        self.name = name

    def credo(self):
        print(f"game {self.name} {self.janr} {self.score} {self.prodoljitelnost}")  # просто нужен для вывода

vndb = vn("sedze-ai,ury", "8.15", "20hr", 'Flowers -Le volume sur ete-')
vndb.credo()
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/5237abbf-50cd-4e00-85a8-3982e9d84408)

## Выводы

Сделали по своему примеру из лабораторки 3
  
## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Everlasting_Summer:
    def __init__(self,janr,score,prodoljitelnost):
        self._janr = janr
        self.__score = score
        self.___prodoljitelnost = prodoljitelnost

    def print_s (self):
        print(f"game {self._janr} {self.__score} {self.___prodoljitelnost}")  # просто нужен для вывода
ruvn = Everlasting_Summer('eroge','7.16','25hr')
ruvn.print_s() # Для запуска первого действия
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/5246e867-d1e6-4237-a51d-e095eb1e3ba7)

## Выводы

Сделали по своему примеру из лабораторки 4
  
## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class ON_OFF:
    def on(self):
        print('включён')

    def off(self):
        print('не включён')


class PEREF:
    def ok(self):
        print('подключено')

    def neok(self):
        print('не подключено')

class PC(ON_OFF, PEREF):
    pass

camera_phone = PC()
camera_phone.on()
camera_phone.off()
camera_phone.ok()
camera_phone.neok()
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/1b634271-519e-4c1d-9404-7274d986d93c)

## Выводы

Сделали по примеру лабораторки из задания 5.

## Общие выводы по теме
самое лучшее изобретение для большого кода.
