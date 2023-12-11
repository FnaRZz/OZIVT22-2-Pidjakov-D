# Тема 11. Итераторы и генераторы.
Отчет по Теме #11 выполнил(а):
- Деревянкин Владислав Владимирович
- ОЗИВТ(ППК)-22-2-у

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
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
### Простой итератор, но у него нет гибкой настройки, например его нельзя развернуть. Он работает просто как next(), но нет prev().

```python
numbers = [0, 1, 2, 3, 4, 5]
for item in numbers:
    print(item)
```

### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/19f6d095-2485-4edf-aa72-96d3f5575a97)

## Выводы
Создали простой итератор без гибкой настройки.

## Лабораторная работа №2
### Класс итератор с гибкой настройкой и удобными применением.

```python
class CountDown:
    def __init__(self, start):
        self.count = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        return self.count

if __name__ == '__main__':
    counter = CountDown(5)
    for i in counter:
        print(i)
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/5cd14842-8746-452b-aa57-68023eb68db7)


## Выводы
Создали сложный итератор с гибкой настройкой.


## Лабораторная работа №3
### Генератор списка.

```python
a = [i ** 2 for i in range(1, 5)]

print('a - ', a)
for i in a:
    print(i)

print('iter(a) - ', iter(a))
for i in a:
    print(i)
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/665d9f6d-932e-47e9-8d35-b2da323d013d)


## Выводы

Создали генератор списка.

## Лабораторная работа №4
### Выражения генераторы.

```python
b = (i ** 2 for i in range(1, 5))
print(b)
print('first')
for i in b:
    print(i)
print('second')
for i in b:
    print(i)
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/2ae33749-aa45-45a1-a8ed-f6c259067804)


## Выводы
Создали генератор

## Лабораторная работа №5
### Такой же счетчик, как и в первом задании, только это генератор и использует yield.

```python
def countdown(count):
    while count >= 0:
        yield count
        count -= 1

if __name__ == '__main__':
    counter = countdown(5)
    for i in counter:
        print(i)
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/bf93f9d1-fd29-445f-9b93-c7643ab421f4)


## Выводы
Сделали счётчик за счёт генератора и использования yield.

## Самостоятельная работа №1
### Вас никак не могут оставить числа Фибоначчи, очень уж они вас заинтересовали. Изучив новые возможности Python вы решили реализовать программу, которая считает числа Фибоначчи при помощи итераторов. Расчет начинается с чисел 1 и 1. Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов. Для реализации этой функции потребуется обратиться к инструкции yield (Она не сохраняет в оперативной памяти огромную последовательность, а дает возможность “доставать” промежуточные результаты по одному). Результатом решения задачи будет листинг кода и вывод в консоль с числом Фибоначчи от 200.

```python
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a
for number in fib(200):
    print(number)
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/57054fb5-f968-44dd-8559-49f698575f11)

## Выводы
Сделали вывол в консоль с числом Фибоначчи

## Самостоятельная работа №2
### К коду предыдущей задачи добавьте запоминание каждого числа Фибоначчи в файл “fib.txt”, при этом каждое число должно находиться на отдельной строчке. Результатом выполнения задачи будет листинг кода и скриншот получившегося файла.

```python
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a

# Пример использования
for number in fib(200):
    print(number)

def write_fibs_to_file(n):
    file = open("fib.txt", "w")
    a, b = 0, 1
    for _ in range(n):
        file.write(str(a) + "\n")
        a, b = b, a + b
    file.close()

#Пример использования
write_fibs_to_file(200)
```
### Результат.
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/23703ac5-5584-4f0a-b615-6335e7adf621)
![image](https://github.com/che3ZzOfficial/Program_engineering/assets/122799788/3628f53d-ba1b-4f19-9f36-9bba6b830844)

## Выводы

Записали числа Фибанначи в файл где каждое число на отдельной строчке.
  
## Общие выводы по теме
Познакомились с итератором,генератором и его ключенвым словом yield.
