# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
from math import *

def main():
    value = int(input('Введите значение: '))
    print(sqrt(value))
    print(sin(value))
    print(cos(value))

if __name__ == '__main__':
    main()