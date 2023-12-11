# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
value = 0
for i in range(10):
    for j in range(10):
        if i != j:
            value += j
        else:
            pass
print(value)