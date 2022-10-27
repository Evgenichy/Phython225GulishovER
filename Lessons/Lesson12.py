# a = {'Tom', 'Bob', 'Alice'}
# a.add('Ann')
# print(a)
# # b = 'Tom'
# # if b in a:
# #     a.remove('Tom')
# # a.discard('Tom')
# a.pop()
# a.clear()
# print(a)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = 'Hello'
# s2 = 'How are you'
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=' ')

# drawing = {'Marina', 'Jenya', 'Sveta'}
# music = {'Kostya', 'Jenya', 'Ilya'}
#
# one = drawing ^ music
# two = drawing & music
# three = drawing - music
# print(one)
# print(two)
# print(three)


# frozenset (Замороженное множество)
# a = frozenset([1, 2, 3, 4, 5])
# print(a)
# s = frozenset({'hello', 'world'})
# print(s)


# Словарь dict()

# lst = ['one', 'two', 'three']
# print(lst)
# print(lst[0])
# d = {'a': 'one', 'b': 'two', 'c': 'three'}
# print(d)
# print(d['a'])

# d = {}
# print(d)
# print(type(d))

# d = {'one': 1, 2: "two"}
# print(d)

# d = dict(short='dict', long='dictionary')
# print(d)


# users = (
#     ('igor@mail.com', 'Igor'),
#     ('irina@mail.com', 'Irina'),
#     ('iann@mail.com', 'Ann'),
# )
# print(users)
# d_user = dict(users)
# print(d_user)

# d = {i: i ** 2 for i in range(7)}
# print(d)
# print(d[2])
# d[2] = 15
# print(d[2])
# d[9] = 45
# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): 'Кортеж', 42: [2, 3, 4, 5], True: 1}
# print(d)
# print(d[42][1])
# print(d[(1, 2.3)])
#
# print('one' in d)
# print('two' in d)

# key = 'one'
# if key in d:
#     del d[key]
# print(d)

# try:
#     del[key]
# except KeyError:
#     print('Такого элемента нет в словре')
# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): 'Кортеж', 42: [2, 3, 4, 5], True: 1}
# print(d)
#
# for key in d:
#     print(key, '->', d[key])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
#
# print(res)

# d = dict()
# d[1] = input('->')
# d[2] = input('->')
# d[3] = input('->')
# d[4] = input('->')

# d = {i: input('-> ') for i in range(1, 5)}
# print(d)
# dislike = int(input('Какой элемент исключить: '))
# del d[dislike]
# print(d)
# print(len(d))

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670k', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6500],
# }
#
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб.', sep='')
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         k = int(input('Количество: '))
#         goods[n][1] = k
#     else:
#         break
#
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб.', sep='')

# d = {'A': 1, "B": 2, 'C': 3}
# v = d['B']
# print('B =', v)
# value = d.get('E', 'False')
# d.clear
# d2 = d.copy()
# print('D =', d)
# print('D2 =', d2)
# print()
#
# d['E'] = 7
# d2['B'] = 5
#
# print('D =', d)
# print('D2 =', d2)

# d = {'A': 1, "B": 2, 'C': 3}
# a = d.items()
# print(a)
# b = d.keys()
# print(b)
# c = d.values()
# print(c)
#
# for key, val in d.items():
#     print(key, '->', val)

d = {'A': 1, "B": 2, 'C': 3}
# item = d.pop('B')
# print(item)
# print(d)
d.update([('R', 7), ('Q', 9)])
print(d)