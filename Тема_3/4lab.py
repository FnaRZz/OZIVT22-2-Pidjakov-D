# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
numbers = [1,3,4,6,7,8,15,16,73,321,322]
value = int(input('Введите значение переменной: '))
if value in numbers:
    if value % 2 == 0:
        print('Переменная четная и есть в массиве numbers')
    else:
        print('Переменная нечетная и есть в массиве numbers')
else:
    print(f"Переменной нет в массиве numbers и она равна {value}")