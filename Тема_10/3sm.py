# для вывода текущего времени
import time
import datetime
a = datetime.datetime.now()
print (a)

# основной код
def add_two_and_input():
    try:
        user_input = input("Введите число: ")
        result = 2 + float(user_input)
        print(f"Результат сложения 2 и введенного числа: {result}")
    except ValueError:
        print("Ошибка: Неподходящий тип данных. Ожидалось число.")

add_two_and_input()
add_two_and_input()
add_two_and_input()