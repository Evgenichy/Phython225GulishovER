import random as r

# import random импортирует все из рандома
# print(random.random())
# print(random.randint(10, 15))
# print(random.randrange(0, 10, 2))

# from random import randint, randrange  # только определные методы из импорта
#
# print(randint(10, 15))
# print(randrange(0, 10 ,2))
#
# import random as r
#
# print(r.randint(10, 15))
# print(r.randrange(0, 10, 2))
#
# city = ['Moscow', 'Novosibirsk', 'Voronej', 'Sochi', 'Ekaterinburg']
# print(r.choice(city))
#
# s = [55, 66, 77, 88, 99, 50, 20, 40, 30, 60, 70, 80, 90]
# print(r.choice(s))
# print(r.choices(s, k=3))
# r.shuffle(s)
# print(s)
#
# print(r.uniform(5.5, 10.5))
# print(round(r.uniform(5.5, 10.5), 2))

# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)

# Функция агрегирования

# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# x = [r.randint(0, 100) for i in range(10)]
# print(x)
# m = max(x)
# print('Max:', m)
# # x[0] = max(x)
# x.remove(m)
# x.insert(0, m)
# print(x)

# x = [r.randint(-20, 20) for i in range(10)]
# print(x)
# x.sort(reverse=True)
# print(x)


# x = [r.randint(0, 100) for i in range(10)]
# print(x)
# m = min(x)
# print('min:', m)
# n = x.index(m)
# print('index:', n)
# del x[:n]
# print(x)

# n1 = int(input('Input value first list: '))
# n2 = int(input('Input value second list: '))
# a = [r.randint(0, 10) for i in range(n1)]
# b = [r.randint(0, 10) for i in range(n1)]
# print('a =', a)
# print('b =', b)
# c = a + b
# print('c = ', c)
# print('Elements two list without repeat: ')
# print('Common elements for two lists: ')


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12, ]
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t\t')
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x, end='\t\t')
#     print()


# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+', y, '=', x + y)


# m = [[r.randint(-10, 20) for x in range(8)] for y in range(4)]
#
# for row in m:
#     for x in row:
#         print(x, end='\t\t')
#     print()
    # print(row, end='\t\t')

m = [[r.randint(-20, 11) for x in range(3)] for y in range(4)]
n = []
for row in m:
    for x in row:
        if x < 0:
            n.append(x)
        print(x, end='\t\t')
    print()

print('Количество отрицательных элементов:', n)
