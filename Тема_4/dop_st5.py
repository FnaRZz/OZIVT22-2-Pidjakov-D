from sm5 import sm5

a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину сторону b: "))
c = float(input("Введите длину стороне c: "))

area = sm5(a, b, c)

print("Площадь треугольника: ", area)