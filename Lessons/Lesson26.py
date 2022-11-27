# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.veryfi_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.passport = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError('ФИО должно быть строкой')
#         f = fio.split()
#         # print(f)
#         if len(f) != 3:
#             raise TypeError('Неверный формат ФИО')
#         letters = ''.join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         # print(letters)
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError('В ФИО можно использовать только буквы и дефис')
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError('Возраст должен быть числом в диапазоне от 14 до 120 лет')
#
#     @classmethod
#     def veryfi_weight(cls, w):
#         if not isinstance(w,float) or w < 20:
#             raise TypeError('Вес должен быть вещественным числом от 20 до 120 кг')
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError('Серия и номер должны быть строкой')
#         s = ps.split()
#         # print(s)
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError('Неверный формат паспорта')
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def passport(self):
#         return self.__passport
#
#     @passport.setter
#     def passport(self, ps):
#         self.verify_ps(ps)
#         self.__passport = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.veryfi_weight(w)
#         self.__weight = w
#
#
# p1 = UserData('Самосвал Камаз Уралович', 26, '7423 008976', 78.2)
# p1.fio = 'Жигули Камаз Уралович'
# p1.old = 35
# p1.passport = '8100 845678'
# p1.weight = 70.0
# print(p1.__dict__)

#######################################################################
# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         print('Инициализатор базового класса Prop')
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#
#     def __init__(self, *args):
#         print('Переопределенный инициализатор Line')
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}')
#
#
# class Rect(Prop):
#
#     def __init__(self, sp, ep, color='red', width=1, bg='yellow'):
#         super().__init__(sp, ep, color, width)
#         self.background = bg
#
#     def draw_rect(self) -> None:
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width()}, {self.background}')
#
#
# line = Line(Point(1, 2), Point(10, 20), 'green', 3)
# line.draw_line()
# print(line.__width)
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()
# print(line.__dict__)
# print(issubclass(Point, object))
########################################################################################################################
# class Figure:
#
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError
#
#     def area(self):
#         print(f'Площадь {self.color} прямоугольника: ', end='')
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, 'blue')
# print(rect.width)
# print(rect.height)
# print(rect.color)
# print(rect.area())
##############################################################################
class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'

    def is_digit(self):
        if not isinstance(self.__x, (int, float)) and not isinstance(self.__y, (int, float)):
            print('Координаты должны быть числами')
            return False
        return True


class Prop:

    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def set_coords(self, sp, ep):
        if sp.is_digit() and ep.is_digit():
            self._sp = sp
            self._ep = ep


class Line(Prop):

    def draw_line(self) -> None:
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')


class Rect(Prop):

    def draw_rect(self) -> None:
        print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')


line = Line(Point(1, 2), Point(10, 20), 'green', 3)
line.draw_line()
line.set_coords(Point(10, 20), Point(100, 200))
line.draw_line()

rect = Rect(Point(7, 9), Point(12, 15))
rect.draw_rect()
rect.set_coords(Point(30, 40), Point(50, 60))
rect.draw_rect()
