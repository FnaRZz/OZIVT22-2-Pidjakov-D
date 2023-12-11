# для вывода текущего времени
import datetime
r = datetime.datetime.now()
print (r)

# основной код
import math

def sm5(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
    a = int(input("Введите длину стороны a: "))
    b = int(input("Введите длину стороны b: "))
    c = int(input("Введите длину стороны c: "))

    area = heron_area(a, b, c)

print("Площадь треугольника:", sm5)
