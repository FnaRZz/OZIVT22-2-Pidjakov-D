# для вывода текущего времени
import time
import datetime
a = datetime.datetime.now()
print (a)

# основной код
from collections import Counter

def count_digits(sequence):
    digit_count = Counter(sequence)
    top_three = dict(sorted(digit_count.items(), key=lambda x: x[1], reverse=True)[:3])
    return top_three

sequence = input("Введите последовательность цифр: ")
result = count_digits(sequence)
print("Самые часто встречающиеся числа:")
for digit in sorted(result.keys()):
    print(f"Число {digit}: {result[digit]} раз(a)")