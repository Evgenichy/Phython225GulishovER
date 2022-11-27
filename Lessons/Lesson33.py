# from Car import electrocar
#
#
# def main():
#     e_car = electrocar.ElectroCar('Tesla', "T", 2018, 99000)
#     e_car.show_car()
#     e_car.description_battery()
#
#
# if __name__ == '__main__':
#     main()
# from math import pi
#
#
# class Rectangle:
#     def __init__(self, l, h):
#         self.l = l
#         self.h = h
#
#     def get_rectangle_perimetr(self):
#         res = self.l * 2 + self.h * 2
#         print(f'Периметр прямоугольника: {res}')
#         return res
#
#     def get_rectangle_area(self):
#         res = self.l * self.h
#         print(f'Площадь прямоугольника: {res}')
#         return res
#
#     def print_rect(self):
#         print(f'Стороны прямоугольника: {self.l}, {self.h}')
#
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def get_circle_circumference(self):
#         res = 2 * pi * self.r
#         print(f'Длина окружности: {round(res, 2)}')
#         return res
#
#     def get_circle_area(self):
#         res = pi * self.r ** 2
#         print(f'Площадь круга: {res}')
#         return res
#
#     def print_circle(self):
#         print(f'Радиус круга: {self.r}')
#
#
# class Cylinder(Rectangle, Circle):
#     def __init__(self, r, h):
#         Circle.__init__(self, r)
#         Rectangle.__init__(self.get_circle_circumference(), h)
#
#     def get_volume(self):
#         res = self.get_circle_area() * self.h
#         print(f'Объем {res}')
#         return res
#
#     def print_cylinder(self):
#         print(f'Радиус основания: {self.r}, высота {self.h}')
#
#
# circles = [Circle(4), Circle(2), Circle(6), Circle(8), Circle(1)]
# rects = [Rectangle(3, 7), Rectangle(2, 7), Rectangle(19, 22)]
# cylinders = [Cylinder(4, 7), Cylinder(2, 5), Cylinder(9, 3), Cylinder(5, 5)]
#
# circle_max_s = max(circles, key=lambda c: c.get_circle_area())
# print(f'Окружность с наибольшей площадью: {circle_max_s.print_circle()} = {round(circle_max_s)}')

# Сериализация

