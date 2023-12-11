# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
one = int(input('Введите значение переменной: '))
if one < 0:
    print('Переменная меньше 0')
elif 0 < one <10:
    print('Переменная больше - и меньше 10')
else:
    print ('Переменная больше 10')