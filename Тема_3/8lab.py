# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
value = 0
while value < 100:
    if value == 0:
        value += 90
    elif value // 5 < 2:
        value *= 5
    else:
        value += 1
    print(value)