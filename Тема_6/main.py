# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
user_input = input("Введите числа через пробел: ")
numbers_list = user_input.split()  # преобразуем строку в список
numbers_tuple = tuple(numbers_list)  # преобразуем список в кортеж

print(f"Список: {numbers_list}")
print(f"Кортеж: {numbers_tuple}")