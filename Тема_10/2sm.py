# для вывода текущего времени
import datetime
import random
a = datetime.datetime.now()
print (a)

# основной код
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            if not data:
                raise Exception("Файл пустой")
            else:
                print("Информация из файла:")
                print(data)
    except Exception as e:
        print(f"Ошибка: {e}")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")


empty_file_path = "empty_file.txt"
open(empty_file_path, 'w').close()

non_empty_file_path = "non_empty_file.txt"
with open(non_empty_file_path, 'w') as file:
    file.write("Hello world.")

print("\nПопытка чтения пустого файла:")
read_file('empty_file.txt')
print("\nПопытка чтения непустого файла:")
read_file('non_empty_file.txt')