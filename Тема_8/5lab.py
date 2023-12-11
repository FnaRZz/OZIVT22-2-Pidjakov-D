# для вывода текущего времени
import datetime
a = datetime.datetime.now()
print (a)

# основной код
class Shape: #Создаем новый класс
    def area(self): #создаем затычку для того чтобы в конце её использовать
        pass #скипаем
class Rectangle(Shape): #Создаем новый класс
    def __init__(self, width, height): #Делаем функцию (метод) с параметрами длины и ширины
        self.width = width # атрибутыч длины
        self.height = height #атрибут ширины

    def area(self): # теперь используем затычку и возвращаем результат на area
        return self.width * self.height #

class Circle(Shape): #новый класс
    def __init__(self, radius): #Делаем функцию (метод) с параметром радиуса
        self.radius = radius #атрибут радиуса прописываем обязательно

    def area(self): #опять используем затычку чтобы через неё выводить ответ
        return 3.14 * self.radius * self.radius #вычисления

shapes = [Rectangle(4, 5), Circle(3)] #теперь заводим данные в них через список
for shape in shapes: #делаем цикл чтобы пройтись по каждому классу
    print(shape.area()) #выводим ответ в консоль
