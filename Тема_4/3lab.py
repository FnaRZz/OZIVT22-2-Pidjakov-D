# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
def main(a,b):
    return a + b

for c in range(5):
    d = main(a=10, b=10)
    print(d)