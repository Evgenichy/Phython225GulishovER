'''
Сделать так, чтобы в классе Line можно было создавать
только целочисленные значения
'''


class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'

    def is_digit(self):
        if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
            print('Координаты должны быть числами')
            return False
        return True

    def is_int(self):
        if not isinstance(self.__x, int) or not isinstance(self.__y, int):
            print('Координаты должны быть целочисленными')
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

    def set_coords(self, sp, ep):
        if sp.is_int() and ep.is_int():
            self._sp = sp
            self._ep = ep


class Rect(Prop):

    def draw_rect(self) -> None:
        print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')


line = Line(Point(1, 2), Point(10, 20), 'green', 3)
line.draw_line()
line.set_coords(Point(10.1, 20), Point(100, 200))
line.draw_line()

rect = Rect(Point(7, 9), Point(12, 15))
rect.draw_rect()
rect.set_coords(Point(30.1, 40), Point(50, 60))
rect.draw_rect()