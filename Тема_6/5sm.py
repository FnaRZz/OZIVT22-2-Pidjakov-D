# для вывода текущего времени
import datetime
r = datetime.datetime.now()
print (r)

# основной код
def find_max_element(input_list):
    max_element = min(input_list)
    return max_element

# Проверка функции на тестах
print(find_max_element([1, 2, 3, 4, 5]))  # ожидаемый результат: 1
print(find_max_element([-1, -2, -3, -4, -5]))  # ожидаемый результат: -5
print(find_max_element([10, 3, 7, 15, 2]))  # ожидаемый результат: 2
