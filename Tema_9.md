# Тема 9.ООП Концепции, принципы 
Отчет по Теме #9 выполнил(а):
-Деревянкин Владислав Владимирович
- ОЗИВТ(ППК)-22-2-у

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | - |
| Задание 3 | + | - |
| Задание 4 | + | - |
| Задание 5 | + | - |
| Задание 6 | - | - |
| Задание 7 | - | - |
| Задание 8 | - | - |
| Задание 9 | - | - |
| Задание 10 | - | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Допустим, что вы решили оригинально и немного странно познакомится с человеком. Для этого у вас должен быть написан свой класс на Python, который будет проверять угадал ваше имя человек или нет. Для этого создайте класс, указав в свойствах только имя. Дальше создайте функцию __init__(), а в ней сделайте проверку на то угадал человек ваше имя или нет. Также можете проверить что будет, если в этой функции указав атрибут, который не указан в вашем классе, например, попробуйте вызвать фамилию.

```python
class Ivan:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Иван':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Иван"

person1 = Ivan('Алексей')
person2 = Ivan('Иван')
print(person1.name)
print(person2.name)
```

### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/92732983-83c5-4b37-a523-ec51c64a2b5e)

## Выводы
побаловались с условием в классах.

## Лабораторная работа №2
### Вам дали важное задание, написать продавцу мороженого программу, которая будет писать добавили ли топпинг в мороженое и цену после возможного изменения. Для этого вам нужно написать класс, в котором Михаил А. Панов будет определяться изменили ли состав мороженого или нет. В этом классе реализуйте метод, выводящий на печать «Мороженое с {ТОППИНГ}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое». При этом программа должна воспринимать как топпинг только атрибуты типа string.

```python
class Icecream:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}")
        else:
            print('Обычное мороженое')

icecream = Icecream()
icecream.composition()
icecream = Icecream('шоколадом')
icecream.composition()
icecream = Icecream(5)
icecream.composition()
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/19f2c16a-59ac-4bed-88c5-3dc753684502)


## Выводы
изи -_-

## Лабораторная работа №3
### Петя – начинающий программист и на занятиях ему сказали реализовать икапсу…что-то. А вы хороший друг Пети и ко всему прочему прекрасно знаете, что икапсу…что-то – это инкапсуляция, поэтому решаете помочь вашему другу с написанием класса с инкапсуляцией. Ваш класс будет не просто инкапсуляцией, а классом с сеттером, геттером и деструктором. После написания класса вам необходимо продемонстрировать что все написанные вами функции работают. Также вас необходимо объяснить Пете почему на скриншоте ниже в консоли выводится ошибка.

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value, "Свойство value")

obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()
print(obj.get_value())
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/90edce9f-face-4756-8ac0-f1a3ed9acc45)


## Выводы

не правильно потому что функция property не так используется

## Лабораторная работа №4
### Вам прекрасно известно, что кошки и собаки являются млекопитающими, но компьютер этого не понимает, поэтому вам нужно написать три класса: Кошки, Собаки, Млекопитающие. И при помощи “наследования” объяснить компьютеру что кошки и собаки – это млекопитающие. Также добавьте какой-нибудь свой атрибут для кошек и собак, чтобы показать, что они чем-то отличаются друг от друга.
```python
class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'

class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'

dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")
cat = Cat()
print(f"Cat is {cat.className}, but they say {cat.sounds}")
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/e5e32fdb-9101-4f5c-9478-c95588ef6955)


## Выводы

сделали собак и кошек отдельно по классам и атрибутам

## Лабораторная работа №5
### На разных языках здороваются по-разному, но суть остается одинаковой, люди друг с другом здороваются. Давайте вместе с вами реализуем программу с полиморфизмом, которая будет описывать всю суть первого предложения задачи. Для этого мы можем выбрать два языка, например, русский и английский и написать для них отдельные классы, в которых будет в виде атрибута слово, которым здороваются на этих языках.А также напишем функцию, которая будет выводить информацию о том, как на этих языках здороваются. Заметьте, что для решения поставленной задачи мы использовали декоратор @staticmethod, поскольку нам не нужны обязательные параметры-ссылки вроде self.

```python
class Russian:
    @staticmethod
    def greeting():
        print("Привет")

class English:
    @staticmethod
    def greeting():
        print("Hello")

def greet(language):
    language.greeting()

ivan = Russian()
greet(ivan)
john = English()
greet(john)
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/f82801d4-a616-4084-a36d-bab33bffd13e)


## Выводы

Сделали полиморфизм

## Самостоятельная работа №1
### Задание:
### Класс Tomato:
1) Создайте класс Tomato
2) Создайте статическое свойство states, которое будет содержать все
стадии созревания помидора
3) Создайте метод ＿ init (), внутри которого будут определены два
динамических свойства: _index (передается параметром) и _state (принимает первое значение из словаря states). После написания этого блока кода в комментарии к нему укажите какими являются эти два свойства 
4)	Создайте метод grow(), который будет переводить томат на следующую стадию созревания 
5)	Создайте метод is_ripe(), который будет проверять, что томат созрел Класс TomatoBush: 
###	Создайте класс TomatoBush 
2)	Определите метод __init__(), который будет принимать в качестве параметра количество томатов и на его основе будет создавать список объектов класса Tomato. Данный список будет храниться внутри динамического свойства tomatoes 
3)	Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания 
4)	Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми. 
5)	Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая Класс Gardener: 
###	Создайте класс Gardener 
1)	Создайте метод __init__(), внутри которого будут определены два динамических свойства: name (передается параметром, является публичным) и _plant (принимает объект класса TomatoBush). После написания этого блока кода в комментарии к нему укажите какими являются эти два свойства 
2)	Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым 
3	Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все, то садовник собирает урожай. Если нет, то метод печатает предупреждение 
4)	Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству
### Тесты: 
1)	Вызовите справку по садоводству 
2)	Создайте объекты классов TomatoBush и Gardener 
3)	Используя объект класса Gardener, поухаживайте за кустом с помидорами 
4)	Попробуйте собрать урожай, когда томаты еще не дозрели. Продолжайте ухаживать за ними 
5)	Соберите урожай 

```python
class Tomato:
    states = {'unripe': 0, 'ripe': 1, 'overripe': 2}

    def __init__(self, index):
        self._index = index
        self._state = self.states['unripe']

    def grow(self):
        if self._state == self.states['ripe']:
            return "Can't grow overripe tomato"
        else:
            next_state = self._state if self._state == 'overripe' else self._state + 1
            self._state = next_state
            return f"Grown tomato #{self._index} from '{self._state}' to '{next_state}'"

    def is_ripe(self):
        return self._state == self.states['ripe']


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def are_all_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name: str, plant: TomatoBush): #name (передается параметром, является публичным) и _plant (принимает объект класса TomatoBush
        self.__name = name
        self.__plant = plant

    @property
    def name(self) -> str:
        return self.__name

    @property
    def plant(self) -> TomatoBush:
        return self.__plant

    def work(self) -> None:
        self.__plant.grow_all()

    def harvest(self) -> bool:
        if not self.plant.are_all_ripe():
            print('Warning: not all fruits are ripe!')
            return False
        else:
            print(f'Harvesting from plant {self.plant}')
            return True

    @staticmethod
    def knowledge_base() -> None:
        print('The static method knowledge_base prints information about gardening.')


gardener = Gardener("John", TomatoBush(10))
gardener.work()
print(gardener.harvest())
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/e4df4249-f19e-48e3-b69d-b096bd952f0f)



В данном коде мы делали постоянные проверки через классы и атрибуты.

## Общие выводы по теме

Научились пользоваться классами и методами по полной.
