# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

#основной код
string = 'hello'
counter = 0
values = [0,2,4,6,8,10]
while counter != 10:
    memory = ' world'
    counter += 1
    if counter in values:
        print(string + memory)
        print(string)
string = string + ' world'
memory = string
string = memory
print (memory)










