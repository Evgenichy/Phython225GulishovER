# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# print(p1.__dict__)
# print(p1.x)
# print(getattr(p1, 'x'))
# print(getattr(p1, 'z', 'False'))
# print(hasattr(p1, 'z'))
# print(hasattr(p1, 'y'))
# # p1.z = 7
# # setattr(p1, 'z', 7)
# setattr(Point, 'z', 7)
# delattr(p1, 'z')
# print(p1.__dict__)

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print('Данные сотрудника: ', self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print('Квалификация сотрудника: ', self.skill, '\n')
#
#
# p1 = Person('Viktor', 'Reznik')
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person('Anna', 'Dolgih')
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     def __new__(cls, *args, **kwargs):
#         print('This is constructor!')
#         return super().__new__(cls)
#
#     def __init__(self):
#         print('This is initializator!')
#
#
# p1 = Point()


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print('Удаление экземпляра: ' + self.__class__.__name__)
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# del p1
# print(p1.x)

# class Point:
#     count = 0  # статические свойства
#
#     def __init__(self, x=0, y=0):  # динамические свойства
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# p2 = Point(15, 20)
# print(Point.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print('Инициализация робота:', self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, 'выключается')
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, 'был последним')
#         else:
#             print('Работающих роботов осталсь:', Robot.k)
#
#     def say_hi(self):
#         print('Приветствую! Меня зовут:', self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print('Численность роботов:', Robot.k)
#
# droid3 = Robot('N2P3')
# droid3.say_hi()
# print('Численность роботов:', Robot.k)
#
# print('\nProcess in progress\n')
#
# print('Роботы закончили свою работую. Давайте их выключим')
# del droid1
# del droid2
# del droid3
# print('Численность роботов:', Robot.k)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(q):
#         if isinstance(q, int) or isinstance(q, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# print(p1.get_coords())
# p1.set_coords(2, 3)
# print(p1.get_coords())
# # print(p1.x, p1.y)
#
# p1.set_x(8)
# print(p1.get_x())
# p1.set_y(13)
# print(p1.get_y())
#
# print(p1.__dict__)
#
# print(p1._Point__x)
# p1._Point__x = 111
# print(p1.__dict__)


class Car:
    def __init__(self, name, year, model, power, color, price):
        self.__name = self.__model = self.__color = 'Неккоректые данные'
        self.__year = self.__power = self.__price = 0
        if Car.__check_value_str(name):
            self.__name = name
        if Car.__check_value_int(year):
            self.__year = year
        if Car.__check_value_str(model):
            self.__model = model
        if Car.__check_value_int(power):
            self.__power = power
        if Car.__check_value_str(color):
            self.__color = color
        if Car.__check_value_int(price):
            self.__price = price

    def __check_value_int(s):
        if not isinstance(s, int):
            print('Данные должны быть числом')
            return False
        return True

    def __check_value_str(s):
        if not isinstance(s, str):
            print('Данные должны быть строкой')
            return False
        return True

    def set_name(self, name):
        if Car.__check_value_str(name):
            self.__name = name

    def get_name(self):
        return self.__name

    def print_info(self):
        print(' Данные автомобиля '.center(40, "*"))
        print(f"""Название модели: {self.__name}
Год выпуска: {self.__year}
Производитель: {self.__model}
Мощность двигателя: {self.__power} л.с.
Цвет машины: {self.__color}
Цена: {self.__price}
""")


c1 = Car('X7 M50i', 2021, 'BMW', 530, 'White', 10790000)
c1.print_info()
c1.set_name('X5')
print(c1.get_name())
c1.print_info()
