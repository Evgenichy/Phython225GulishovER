#ООП (объектно-ориентированное программирование)
class Point:
    '''Класс для предоставления координат точек на плоскости'''
    x = 1
    y = 1

    def set_Coords(self):
        print(self.__dict__)


p1 = Point()
p1.x = 200
p1.y = 5
p1.set_Coords()
# print(type(p1))
# print(p1.x, p1.y) # вызов переменной через класс
# print(id(p1))
# print(id(Point))
# print(p1.__dict__)

# print(Point.__doc__)
# print(Point.__name__)


# p2 = Point()
# print(p2.x, p2.y)
# print(p2.__dict__)
# print(Point.__dict__)