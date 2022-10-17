# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print('Я метод внешнего класса')
#
#     def outer_obj_method(self):
#         print("обычный метод")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_metod(self):
#             print('Я метод внутреннего класса', MyOuter.age, self.obj.name)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('Внешний')
# inner = out.MyInner('внутренний', out)
# inner.inner_metod()


# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print(f"Name: {self.name}")
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light Green'
#
#         def display(self):
#             print(f"Name: {self.name}")
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()
# print(g.name)


# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Employee list:')
#         print(f'Name: {self.name}')
#
#     class Intern:
#         def __init__(self):
#             self.name = 'Smith'
#             self.id = '657'
#
#         def display(self):
#             print(f'Name: {self.name}')
#             print(f'Id: {self.id}')
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#             self.id = '007'
#
#         def display(self):
#             print(f'Name: {self.name}')
#             print(f'Id: {self.id}')
#
#
# outer = Employee()
# outer.show()
#
#
# d1 = outer.intern
# d2 = outer.head
# d1.display()
# d2.display()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print('Class Outer')
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print('Class Inner')
#
#         class InnerClass:
#
#             def show(self):
#                 print('Inner Class')
#
#
# outer = Outer()
# outer.show()
# inner1 = outer.inner
# inner1.show()
# inner2 = outer.inner.inner_inner
# inner2.show()

class Computer:
    def __init__(self):
        self.name = 'PC001'
        self.os = self.OS()
        self.cpu = self.CPU()

    class OS:
        def system(self):
            return 'Windows 10'


    class CPU:
        def make(self):
            return 'Intel'

        def model(self):
            return 'Core i7'


comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
my_os = Computer.OS()
my_cpu = Computer.CPU()
print(comp.name)
print(my_os.system())
print(my_cpu.make())
print(my_cpu.model())
 # 1:53