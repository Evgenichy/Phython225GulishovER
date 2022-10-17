# n = int(input('Укажите кол-во символов: '))
# sim = input('Тип символа: ')
# orient = int(input('0 - горизонтальная\n1 - вертикальная\nориентация линии: '))
# i = 0
# while i < n:
#     if orient == 0:
#         print(sim, end=' ')
#     elif orient == 1:
#         print(sim)
#     else:
#         print('Такой ориентации нет')
#         break
#     i += 1


# num = int(input('Введите кол-во чисел последовательности: '))
# i = 1
# n = float(input('Введите число: '))
# sum = n
# min = n
# max = n
# while i < num:
#     n = float(input('Введите число: '))
#     sum += n
#     if max < n:
#         max = n
#     if min > n:
#         min = n
#     i += 1
# print('Среднее арифметическое равно:', sum/n)
# print('Максимальное число:', max)
# print('Минимальное число:', min)

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j, end='\t\t')
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print('^', end=' ')
#         j += 1
#     print()
#     i += 1

# i = 0    #My code
# while i < 3:
#     j = 0
#     while j < 16:
#         print('+', end='')
#         j += 1
#         k = 0
#     print()
#     while k < 16:
#         print('-', end='')
#         k += 1
#     print()
#     i += 1

# teacher code
# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1

# for "element" in "collection":
#      print("element")


# for i in 5, 6, 7, 8, 9:
#     print(i)

# for i in 'Hello':
#    print(i)


# range(start, stop, step)
# print(range(4, 6))

# for i in range(1, 6, 1):
#     print(i)

# a = int(input('Ввежите целое число: '))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=' ')

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=' ')

# for i in range(3):
#     print(i, end=' ')
#     if i == 1:
#         break
# else:
#     print('done')

# for i in range(3):
#     print('+++')
#     for j in range(2):
#         print('-----')

# w = int(input('Width: '))
# h = int(input('High: '))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h -1 or j == 0 or j == w - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()


# n = [i for i in range(6) if i % 2 == 0]
# print(n)

# n = [i*2 for i in 'Hello']
# print(n)

# Список
# n = [5, 6, 7, 8, 9]
# print(n)
# print(type(n))

# s = [1, 2, 3]
# print(s)
#
# b = list('hello')  # преобразование других типов данных в список
# print(b)

# s = [1, 2, 3]
# print(s * 2)

# time: 2:32
