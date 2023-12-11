import datetime
r = datetime.datetime.now()
print (r)
def dd(func): # создаём новый метод в котором будет вложенный метод с проверкой
    def wrapper(*args, **kwargs):
        print(f"Декоратор: Вызывается функция {func.__name__}") # запрашивается функция
        result = func(*args, **kwargs) # выполнение функции
        print(f"Декоратор: Функция {func.__name__} выполнена") # отписка что функция выполнена
        return result # возвращаем результат.
    return wrapper
@dd # первая функция
def add_numbers(a, b):
    return a / b

@dd # вторая функция
def multiply_numbers(a, b):
    return a ** b

result_sum = add_numbers(2, 3) # данные
print(f"Результат сложения: {result_sum}") # вывод в консоль

result_product = multiply_numbers(4, 5)# данные
print(f"Результат умножения: {result_product}") # вывод в консоль