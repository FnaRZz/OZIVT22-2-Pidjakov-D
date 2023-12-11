import datetime
r = datetime.datetime.now()
print (r)
class Everlasting_Summer:
    def __init__(self,janr,score,prodoljitelnost):
        self._janr = janr
        self.__score = score
        self.___prodoljitelnost = prodoljitelnost

    def print_s (self):
        print(f"game {self._janr} {self.__score} {self.___prodoljitelnost}")  # просто нужен для вывода
ruvn = Everlasting_Summer('eroge','7.16','25hr')
ruvn.print_s() # Для запуска первого действия