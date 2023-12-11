# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
def mean(*args):
   try:
      return sum(args) / len(args)
   except ZeroDivisionError:
      return 'Error'

# Test code
if __name__ == "__main__":
   print(mean(1, 2 , 3))