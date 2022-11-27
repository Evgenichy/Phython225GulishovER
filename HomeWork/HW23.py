from math import sqrt


class Rectangle:
    def __init__(self,  length, weight):
        self.__length = self.__weight = 0
        if Rectangle.__check_value_int(length):
            self.__length = length
        if Rectangle.__check_value_int(weight):
            self.__weight = weight

    def __check_value_int(s):
        if not isinstance(s, int):
            print('Данные должны быть числом')
            return False
        return True

    def set_length(self, length):
        if Rectangle.__check_value_int(length):
            self.__length = length

    def get_length(self):
        return self.__length

    def set_weight(self, weight):
        if Rectangle.__check_value_int(weight):
            self.__weight = weight

    def get_weight(self):
        return self.__weight

    def square(self):
        a = self.__weight * self.__length
        print("Площадь прямоугольника:", a)

    def area(self):
        s = (self.__length + self.__weight) * 2
        print('Периметр прямоугольника:', s)

    def hypotenuse(self):
        h = sqrt(self.__length ** 2 + self.__weight ** 2)
        print('Гипотенуза прямоугольника:', round(h, 2))

    def figure(self):
        for i in range(self.__length):
            for j in range(self.__weight):
                print('*', end='')
            print()


r = Rectangle(3, 9)
print('Длина прямоугольника:', r.get_length())
print('Ширина прямоугольника:', r.get_weight())
r.get_weight()
r.get_length()
r.area()
r.square()
r.hypotenuse()
r.figure()
