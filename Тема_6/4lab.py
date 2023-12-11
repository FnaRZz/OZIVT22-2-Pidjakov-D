# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
def personal_info(name, age, company='unnamed'):
    print(f"Имя: {name} Возраст: {age} Компания: {company}")

tom = ("Григорий", 22)
personal_info(*tom)

bob = ("Григорий", 41, "Yandex")
personal_info(*bob)