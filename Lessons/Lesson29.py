# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#
# class Styles:
#     def __init__(self, color='red', width=1):
#         print('Инициализатор Styles')
#         self._color = color
#         self._width = width
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print('Инициализатор Pos')
#         self._sp = sp
#         self._ep = ep
#         super().__init__(*args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# l1 = Line(Point(10,10), Point(100, 100), 'green', 5)
# l1.draw()

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='Logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubclass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclasslog.txt')
#
#
# subclass = MySubclass()
# subclass.display(' Это страка будет отображаться и записываться в файл')


# class Goods:
#     def __init__(self, name, weight, price):
#         print('Инициализатор Goods')
#         self.name = name
#         self.weihgt = weight
#         self.price = price
#
#     def price_info(self):
#         print(f'{self.name}, {self.weihgt}, {self.price}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print('Инициализатор MixinLog')
#         self.ID += 1
#         self.id = self.ID
#
#     def save_log(self):
#         print(f'{self.id}: Товар был продан в 00:00 часов')
#
#
# class Notebook(Goods, MixinLog):
#     pass
#
#
# n = Notebook('HP', 1.5, 35000)
# n.price_info()
# n.save_log()
# print(Notebook.__mro__)


class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError('Секунды должны быть целым числом')

        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else '0' + str(x)


c1 = Clock(100)
print(c1.get_format_time())