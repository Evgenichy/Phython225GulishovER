# class Integer:
#     @classmethod
#     def verify_coords(cls, coords):
#         if not isinstance(coords, int):
#             raise TypeError(f'Координата {coords} должна быть числом')
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_coords(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
# class Point3d:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3d(1, 2, 3)
# print(p1.__dict__)

####################################################################
# Метаклассы

# a = 5
# print(a)
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)

# MyList = type(
#     'MeList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# lst[0] = 3
# print(lst, lst.get_length())

#type(
# имя класса(в виде строкого значения)
# кортеж родительских классов
# словарь, содержащий атрибуты(свойства и методы) и их значения
#
# )


# class MyMetaClass(type):
#     def __new__(cls, name, bases, attr):
#         print('Создание нового объекта', name)
#         return super(MyMetaClass, cls).__new__(cls, name, bases, attr)
#
#     def __init__(cls, *args, **kwargs):
#         print('Инициализация класса', args[0])
#         super(MyMetaClass, cls).__init__(*args, **kwargs)
#
#
# class Student(metaclass=MyMetaClass):
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# stud = Student('Anne')
# print("Student's name: ", stud.get_name())
# print('Type object Student: ', type(stud))
# print('Type object Student: ', type(Student))

############################################################
# Создание модулей

# import geometry.tria
# import geometry.rect
# import geometry.sq

from geometry import rect, sq, tria
# from geometry import *

r1 = rect.Rectangle(1, 2)
r2 = rect.Rectangle(3, 4)

s1 = sq.Square(10)
s2 = sq.Square(20)

t1 = tria.Triangle(1, 2, 3)
t2 = tria.Triangle(4, 5, 6)

shape = [r1, r2, s1, s2, t1, t2]
for g in shape:
    print(g.get_perimetr())

