#ООП (объектно-ориентированное программирование)
# class Point:
#     '''Класс для предоставления координат точек на плоскости'''
#     x = 1
#     y = 1
#
#     def set_Coords(self):
#         print(self.__dict__)
#
#
# p1 = Point()
# p1.x = 200
# p1.y = 5
# p1.set_Coords()
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


# class Point:
#     x = 1
#     y = 1
#
#     def set_coords(self):
#         print(self.__dict__)
#
#
# p1 = Point()
# p1.x = 200
# p1.y = 5
# p1.set_coords()


# class Point:
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coords(5, 10)
# print(p1.__dict__)


class Human:
    name = 'name'
    birthday = '00.00.0000'
    phone = '00-00-00'
    country = 'country'
    city = 'city'
    address = 'street, house'

    def print_info(self):
        print(' Персональные данные '.center(40, '*'))
        print(f'Имя: {self.name}\n'
              f'Дата рождения: {self.birthday}\n'
              f'Номер телефона: {self.phone}\n'
              f'Страна: {self.country}\n'
              f'Город: {self.city}\n'
              f'Домашний адресс: {self.address}')
        print('=' * 40)

    def input_info(self, first_name, birthday, phone, country, city, address):
        self.name = first_name
        self.birthday = birthday
        self.phone = phone
        self.country = country
        self.city = city
        self.address = address

    def set_name(self, name):  # устанавливаем имя
        self.name = name

    def get_name(self):  # получить имя
        return self.name

    def set_birthday(self, birthday):
        self.birthday = birthday

    def get_birthday(self):
        return self.birthday


h1 = Human()
h1.input_info('Юля', "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
h1.print_info()
h1.set_name('Валерия')
print(h1.get_name())
h1.set_birthday('23.05.1986')
print(h1.get_birthday())
