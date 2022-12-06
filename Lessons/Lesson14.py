def func(a, *args):
    return a, args


print(func(1))
print(func(1, 2, 3, "abc"))


def print_scores(student, *scores):
    print("Student Name: " + student)
    for score in scores:
        print(score)


print_scores("Irina", 100, 95, 88, 92, 99)
print_scores("Igor", 96, 20, 33)


def func(**kwargs):
    return kwargs


print(func(a=1, b=2, c=3))
print(func())
print(func(a="python"))


def intro(**data):
    for key, value in data.items():
        print(key, 'is', value)
    print()


intro(first_name="Irina", last_name="Fokina", age=22)
intro(first_name="Igor", last_name="WOOD", email='igor@gmail.com', age=25, phone='9594567895')


def db(**kwargs):
    my_dict.update(kwargs)


my_dict = {'one': 'first'}
db(k1=22, k2=31, k3=11, k4=91)
db(name='Bob', age='31', weight=61, eyes_color='gray')
print('my_dict =', my_dict)


def db(b, c, w, *args, name, **kwargs):
    print(b, c, w, args, name, kwargs)


db(7, 8, 9, a=5, name='Olga', q=5)

name = 'Tom'  # глобальная область видимости


def hi():
    global name
    name = 'Sam'  # локальная область видимости
    print("Hello", name)


def bye():
    print("Good bye", name)


# print(name)
hi()
# bye()
print(name)

i = 5


def func(arg=i):
    print("i =", i)
    print("arg =", arg)


i = 6
func()  # 5 или 6

x = 4


def add_two(a):
    # x = 2

    def add_some():
        # x = 5
        print('x =', x)
        return a + x

    return add_some()


print(add_two(3))

import builtins

names = dir(builtins)

for t in names:
    print(t)

min = [4, 5, 6]
print(max(min))
print(min(min))


def outer_func(who):
    def inner_func():
        print("Hello,", who)

    inner_func()


outer_func("World!!!")

a = 2


def func1():
    a = 6

    def func2(b):
        global a
        a = 4
        print("Сумма:", a + b)

    print("Значение переменной a:", a)
    func2(4)


func1()
print(a)


def fn1():
    x = 25  # 1

    def fn2():
        # x = 33  # 3

        def fn3():
            nonlocal x
            x = 55  # 5
            print("fn3.x =", x)  # 6

        fn3()  # 4
        print("fn2.x =", x)  # 7

    fn2()  # 2
    print("fn1.x =", x)  # 8

fn1()


def outer(a1, b1, a2, b2):
    a = 0
    b = 0

    def inner():
        nonlocal a, b
        a = a1 + a2
        b = b1 + b2

    inner()
    return [a, b]


res = outer(2, 3, -1, 4)
print(res)


def increment(number):
    def inner(x):
        return number + x
    return inner


a = increment(10)
print(a(5))
print(a(4))

b = increment(1)
print(b(7))

print(increment(5)(10))


def func1():
    a = 1
    b = 'line'
    c = [1, 2, 3]

    def func2():
        nonlocal a, b
        c.append(4)
        a = a + 1
        b = b + "_new"
        return a, b, c

    return func2


func = func1()
print(func())


def func(city):
    s = 0

    def inner():
        nonlocal s
        s += 1
        print(city, s)

    return inner


res1 = func('Москва')
res1()
res1()

res2 = func('Сочи')
res2()
res2()
res2()
res2()

res1()


student = {
    'Alice': 98,
    'Bob': 67,
    'Chris': 85,
    'David': 75,
    'Elise': 54,
    'Fiona': 35,
    'Grace': 69
}


def make_classifier(lower, upper):
    def students(exem):
        return {k: v for k, v in exem.items() if lower <= v < upper}

    return students


a = make_classifier(80, 100)
b = make_classifier(70, 80)
c = make_classifier(50, 70)
d = make_classifier(0, 50)

print(a(student))
print(b(student))
print(c(student))
print(d(student))
