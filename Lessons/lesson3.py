# Исключения

# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n // m)
# except (ValueError, ZeroDivisionError):
#     print('Invalid data')
# else:
#     print('All good. You write num', n, 'and', m)
# finally:
#     print('End of program')


# except ValueError:
#     print('Нельзя вводить строки')
# except ZeroDivisionError:
#     print('You can`t delete on zero')

# print('OK!')


# n = input('Введите первое число: ')
# m = input('Введите второе число: ')
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
#     m = str(m)
# finally:
#     print(n + m)


# while условие:
#     блок инструкий

# i = 10  # переменная счетчик
# while i > 0:
#     print('i =', i)
#     i -=1  # i = i+ 1


# i = 1
# while i <= 20:
#     if i % 2:
#         print(i, end=' ')
#     i += 1

# i = 1
# while i <= 1000:
#     print(i, end=' ')
#     i *= 10


# a = int(input('Укажите кол-во символов: '))
# i = 0
# while i < a:
#     print('*', end='')
#     i += 1


# a = int(input('Укажите кол-во символов: '))
# while a > 0:
#     print('*', end='')
#     a -= 1

# Написать программу , которая находит сумму всех нечетных чисел

# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
# i = a
# res = 0
# while i <= b:
#     if i % 2 != 0:
#         res += i
#         # print(i, end=' ')
#     i += 1
# print('Sum:', res)


# n = input('Введите целое число: ')
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('Chislo ne celoe')
#         n = input('Введите целое число: ')
#
# if n % 2 == 0:
#     print("Chetnoe")
# else:
#     print("Nechetnoe")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\nloop is done')


# i = 0
# while True:
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input('Input positive number: '))
#     if not n < 0:
#         break
# print(n)

# res = 1
# while True:
#     n = int(input('Input number: '))
#     if n == 0:
#         break
#     res *= n
# print('resalt:', res)


# i = 0
# while i < 10:
#     print(i, end=' ')
#     i += 1
# else:
#     print('\nLoop is done, i =', i)
