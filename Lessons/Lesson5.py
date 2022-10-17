# n = list(range(2, 10, 2))
# n2 = [2, 4, 6, 8]
# print(n)
# print(id(n))
# print(n2)
# print(id(n2))
# if n is n2:
#     print('List is  =')
# else:
#     print('List is !=')

# [выражение for переменная in последовательность]
# n = 5
# a = [0 for i in range(5)]
# a2 = [i ** 2 for i in range(1, n + 1)]
# print(a2)
#
# for i in range(1, n + 1):
#     print(i ** 2, end=' ')

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input('Введите количество элементов списка: '))
# print(a)
# for i in range(len(a)):
#     a[i] = input('-> ')
# print(a)

# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# print(a)

# print([int(input('-> ')) for i in range(int(input('n = ')))])


# n = [2, 4, 6, 8]
# #
# # for i in range(len(n)):
# #     print(n[i], end=' ')
# #
# print()
# for elem in n:
#     print(elem, end=' ')

# a = [int(input('n = ')) for i in range(int(input('Элементов списка: ')))]
# b = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         b += a[i]
# print(b)


# n = list(range(21, 41))
# print(n)
# s = k = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
#
# print('Кол-во:', k)
# print('sum:', s)


# n = [int(input('-> ')) for i in range(int(input('Элементов списка: ')))]
# s = k = 0
# for i in range(len(n)):
#     if n[i] != 0:
#         s += n[i]
#         k += 1
# print(s / k)



