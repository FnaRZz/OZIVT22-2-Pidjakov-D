# для вывода текущего времени
import datetime
import random
a = datetime.datetime.now()
print (a)

# основной код
def dice_roll():
    roll = random.randint(1, 6)
    print("Кубик выпал на:", roll)
    if roll in [5, 6]:
        print("Вы выиграли!")
    elif roll in [3, 4]:
        dice_roll()
    else:
        print("Вы проиграли")
dice_roll()