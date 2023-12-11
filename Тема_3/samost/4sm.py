# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

#основной код
sentence = input("Введите предложение на английском: ")
lower_sentence = sentence.lower()
print("Предложение в нижнем регистре:", lower_sentence)
vowels = ['a', 'e', 'i', 'o', 'u']
count_vowels = 0
for char in lower_sentence:
    if char in vowels:
        count_vowels += 1
print("Количество гласных:('a', 'e', 'i', 'o', 'u')", count_vowels)

replace_sentence = lower_sentence.replace("ugly", "beauty")
print("Замененное предложение:", replace_sentence)
if lower_sentence.startswith("the"):
    print("Предложение начинается с 'The'")
else:
    print("Предложение не начинается с 'The'")

if lower_sentence.endswith("end"):
    print("Предложение заканчивается на 'end'")
else:
    print("Предложение не заканчивается на 'end'")