# для вывода текущего времени
import datetime
r = datetime.datetime.now()
print (r)

# основной код
# Custom exception class
class CustomException(Exception):
    pass

# Code snippet 1
def divide_numbers(a, b):
    if b == 0:
        raise CustomException("Нельзя делить на ноль")
    return a / b

try:
    result = divide_numbers(10, 0)
    print("Результат:", result)
except CustomException as e:
    print("Ошибка:", str(e))

# Code snippet 2
def process_data(data):
    if not data:
        raise CustomException("Данные не предоставлены")
    # Process the data here

try:
    process_data([])
except CustomException as e:
    print("Ошибка:", str(e))
