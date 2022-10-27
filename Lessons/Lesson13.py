# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')

# print(d)
# print(new_d)

# a = {
#     'First': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'Second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ': ', a[x][y], sep='')

# sales = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
# }
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ': ', sales[x][y], sep='')
#
# person = input('Name: ')
# region = input('Region: ')
# print(sales[person][region])
# data = int(input('New data: '))
# sales[person][region] = data
# print(sales[person])

# data = {"one": 1, "two": 2, "three": 3, "four": 4}
# d = {k: v for k, v in data.items() if v <= 2}
# print(d)
# data['one'] = 5
# print(data)
# print(d)

# s = 'Hello'
# b = {i: i *2 for i in s}
# print(b)
# a = list(b.values())
# print(a)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []  # d['one'] = []
#         s = i  # s = 'one'
#     else:
#         d[s].append(i)
# print(d)

# zip

# d = dict(zip([12, 1, 2], ['Dec', 'Jen', 'Feb']))
# print(d)

# a = ['Dec', 'Jen', 'Feb']
# b = [12, 1, 2]
# d = {k: v for k, v in zip(b, a)}
# print(d)

# a = ['a', 'b', 'c', 'd']
# b = [12, 1, 2]
# c = [4.0, 5.0, 6.0]
# q = zip(a, b, c)
# print(list(q))

# print(list(zip(range(100), range(5))))

# one = {'name': 'Igor', 'Last_name': 'Smith', 'Job': 'Consultant'}
# two = {'name': 'Olga', 'Last_name': 'Doe', 'Job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# Распаковка последовательностей
# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)
#

# month = ['January', 'February', 'March']
# total_sales  = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print('Общая прибыль в', m, '=', profit)


# one = {'apple': 20, 'ornge': 35}
# two = {'pepper': 40, 'onion': 55}
# print({**two, **one})


# for i in range(3):
#     print(i)
#
# colors = ['red', 'yellow', 'green']
# j = 1
# for i in colors:
#     print(j, i)
#     j += 1


# colors = ['red', 'yellow', 'green']
# for j, i in enumerate(colors, 1):
#     print(j, i)

# num_list = [1, 2, 3, 4, 5]
# i = iter(num_list)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*a):
#     return a
#
#
# print(func(2))
# print(func(2, 1, 3))
# print(func())


# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(7, 3))


# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))


def ch(*args):
    res = []
    sr_ar = sum(args) / len(args)
    print(sr_ar)

    for i in args:
        if i < sr_ar:
            res.append(i)

    return res


print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(ch(3, 6, 1, 9, 5))
