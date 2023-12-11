# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

#основной код
num = int(input())
if num < 0 or num > 10:
    print("Число не подходит по требованиям")
elif num >= 0 and num <= 3:
    print("от 0 до 3 включительно")
elif num > 3 and num <= 6:
    print("от 3 до 6")
elif num > 6 and num <= 10:
    print("от 6 до 10 включительно")