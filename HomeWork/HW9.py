from math import pi


def get_rectangle():
    if r == 1:
        a = int(input('Введите ширину: '))
        b = int(input('Введите высоту: '))
        print("Площадь:", a + b)


def get_triangle():
    if r == 2:
        a = int(input('Введите высоту: '))
        b = int(input('Введите основание: '))
        print("Площадь:", (a * b) * 0.5)


def get_circle():
    if r == 3:
        a = int(input('Введите радиус: '))
        print("Площадь:", int(pi * a ** 2))


r = int(input("Найти площадь фигуры:\n0 - выход\n1 - прямоугольник\n2 - треугольник\n3 - круг"
                    "\nВыбор из списка: "))


def done():
    if r == 0:
        print('Завершение программы')
        exit()


if r > 4:
    print('Error')

get_rectangle()
get_triangle()
get_circle()
done()







