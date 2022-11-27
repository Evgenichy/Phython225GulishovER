"""Создать класс для преобразования кг в фт
-Создать класс с закрытым инициализатором который принимает кг
-Создать декоратор Property
-Создать _get_ _set_ из декоратора
- Сделать проверку в _set_ чтобы можно было вводить только числовые значения
- 1 метод который переводит из кг в фт

class (Name):
    def __init__

    @Property
    def __get__

    def __set__
        if _check_value_int_

    def (преобразование)"""


class Converting:

    def __init__(self, kg=0):
        self.__kg = 0
        if Converting.__check_value_int(kg):
            self.__kg = kg
        #self.__ft = ft

    def __check_value_int(s):
        if not isinstance(s, int):
            print('Киллограммы задаются только числами')
            return False
        return True

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, k):
        if Converting.__check_value_int(k):
            self.__kg = k

    def conv(self):
        s = self.__kg * 2.205
        print(f'{self.__kg} кг =>', s, 'фунтов')


c1 = Converting(12)
c1.conv()
