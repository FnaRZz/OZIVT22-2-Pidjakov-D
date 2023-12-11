# для вывода текущего времени
import time
import datetime
a = datetime.datetime.now()
print (a)

# основной код
def get_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

start = time.time()
for _ in range(5):
    current_time = get_time()
    print(current_time)
    time.sleep(1)
    elapsed_time = time.time() - start
print("Программа выполнялась", elapsed_time, "секунд")