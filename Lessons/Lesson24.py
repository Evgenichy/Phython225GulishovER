# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def coord_x(self):  # __get_x
#         print('Вызов __get_x')
#         return  self.__x
#
#     @coord_x.setter
#     def coord_x(self, x):  # __set_x
#         print('Вызов __set_x')
#         self.__x = x
#
#     @coord_x.deleter
#     def coord_x(self):  #__del_x
#         print("удаление свойства")
#         del self.__x
#
#     # cord_x = property(__get_x, __set_, __del_x)
#
#
# p1 = Point(5, 10)
# p1.coord_x = 100  # установить значение
# print(p1.coord_x)  # получить значение
# del p1.coord_x
# p1.coord_x = 7
# print(p1.__dict__)


# class Person:
#
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# p1 = Person('Irina', 26)
# print(p1.name)
# p1.name = 'Igor'
# del p1.name
# print(p1.__dict__)


# class Person:
#
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, o):
#         self.__old = o
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person('Irina', 26)
# print(p1.old)
# p1.old = 28
# del p1.old
# print(p1.__dict__)


# class Point:
#     __count = 0  # статическое свойство(переменная)
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# print('p1 =', Point.get_count())
# p2 = Point()
# print('p2 =', Point.get_count())
# p3 = Point()
# print('p3 =', Point.get_count())

# print(Point.get_count())


# class Change:

#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))


# class Numbers:

#     @staticmethod
#     def min(a, b, c, d):
#         minim = min(a, b, c, d)
#         return minim
#
#     @staticmethod
#     def max(a, b, c, d):
#         maxim = max(a, b, c, d)
#         return maxim
#
#     @staticmethod
#     def sr_arifm(a, b, c, d):
#         arifm = (a + b + c + d) / 4
#         return arifm
#
#     @staticmethod
#     def factor(a):
#         count = 1
#         for i in range(1, a + 1):
#             count = count * i
#             # print(count)
#         return count
#
#
# print('Минимальное число:', Numbers.min(1, 9, 2, 8))
# print('Максимальное число', Numbers.max(1, 9, 2, 8))
# print('Среднее арифметичекое', Numbers.sr_arifm(1, 9, 2, 8))
# print('Факториал числа', Numbers.factor(5))


class Date:
    def __init__(self, day=0,month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def string_to_db(self):
        return f'{self.year}-{self.month}-{self.day}'

    @classmethod
    def from_string(cls, data_as_string):
        d, m, y = map(int, data_as_string.split('.'))
        return cls(d, m, y)

    @staticmethod
    def is_date_valid(data_as_string):
        if data_as_string.count('.') == 2:
            d, m, y = map(int, data_as_string.split('.'))
            return d <= 31 and m <= 12 and y <= 3999


dates = [
    '30.12.2020',
    '30-12-2020',
    '01.31.2021',
    '12.31.2020'
]
for string_date in dates:
    if Date.is_date_valid(string_date):
        date = Date.from_string(string_date)
        string_to_db = date.string_to_db()
        print(string_to_db)
    else:
        print('Некоректная дата')

# d1 = Date.from_string('12.11.2022')
# print(d1.string_to_db())

# string_date = '20.10.2022'
# d, m, y = map(int, string_date.split('.'))
#
# d1 = Date(d, m, y)
# print(d1.string_to_db())



#2:55:00