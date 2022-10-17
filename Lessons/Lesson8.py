import math
import time
import locale


# num1 = math.sqrt(2)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)

# r = int(input('Введите радиус окружности: '))
# print('Длина окружности:', round(2 * math.pi * r, 2))


# seconds = time.time()
# print('Секунды с начала эпохи:', seconds)
# locale_time = time.ctime()
# print('Местное время:', locale_time)
# locale_time2 = time.localtime()
# print(locale_time2)
# print(locale_time2.tm_mday, '.', locale_time2.tm_mon, '.', locale_time2.tm_year, sep='')
# print(time.strftime('Today is %B %d, %Y.'))
# print((time.strftime('%d/%m/%Y, %H:%M:%S', time.localtime(46468522))))

# pause = 5
# print('Programe start...')
# time.sleep(pause)
# print(pause, 'seconds')

# text = input('название напоминания: ')
# locale_time = float(input('Через сколько минут: '))
# locale_time = locale_time * 60
# time.sleep(locale_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, 'seconds')

# start = time.monotonic()
# time.sleep(5)
# res = time.monotonic() - start
# print(res, 'seconds')


# locale.setlocale(locale.LC_ALL, 'ru')
# print(time.strftime('Сегодня %B %d, %Y.'))

# Функиции

# def hello(name):  # аргументы
#     print('Hello',name)
#
#
# hello('Irina')  # параметры
# hello
#
# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)


# def symbol(a, b, c):
#     for i in range(a):
#         if i % 2 == 0:
#             print(b, end='')
#         else:
#             print(c, end='')
#     print()
#
# symbol(9, '+', '-')
# symbol(7, 'X', '0')

# def get_sum(a, b):
#     return a + b
#
#
# res = get_sum(1, 8)
# print(res)
#
# print(get_sum(2, 5))


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))

# n = int(input("a: "))
# m = int(input("b: "))


# def res(a, b):
#     if a > b:
#         return a - b
#     if a < b:
#         return a + b
#
#
# print(res(n, m))

# def cube(a):
#     return a ** 3
#
# for i in range(1, 11):
#     print(i, 'in cube =', cube(i))

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a , end=' ')
        a, b = b, a + b


fib(15)
