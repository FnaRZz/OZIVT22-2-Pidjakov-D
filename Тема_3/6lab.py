# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
string = 'Привет всем изучающим Python!'
value = input()
for i in string:
    if i == value:
        index = string.find(value)
        print(f"Буква '{value}'есть в строке под {index} индексом")
        break
else:
    print(f"Буква '{value}'нет в указанной строке")