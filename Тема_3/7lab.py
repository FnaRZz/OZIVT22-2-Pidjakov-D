# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
value = 100
for i in range(10,-1,-1):
    value -= i
    print(i, value)