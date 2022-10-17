# # Кортеж
#
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
#
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = ()
# print(type(a))
# b = tuple()
# print(type(b))

# t = (1)
# print(type(t))

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return  tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
#
# print(slicer((1, 2, 3,), 8))
# print(slicer((1, 2, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)
# print(type(x))
# print(type(t))


# def get_user():
#     name = 'Evgenichy'
#     age = 23
#     is_married = False
#     return name, age, is_married
#
#
# user1, user2, user3 = get_user()
# print(user1)
# print(user2)
# print(user3)

# t = (1, 2, 3)
# del t
# print(t)

# lst = [1, 2, 3, 4, 5, 6]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)

countries = (
    ('Германия', 20.2, (('Берлин', 3.326), ('Гамбург', 1.178))),
    ('France', 66, (('Marsele', 1.6),('Paris', 2.2)))
)
print(countries)

for country in countries:
    country_name, country_population, cities = country
    print("\nСтрана:", country_name, "население =", country_population)
    for city in cities:
        city_name, city_population = city
        print("\tГород:", city_name, "население =", city_population)

# Множества (set) - неупорядоченная коллекция, которая хранит только уникальные значения

# {}
set()

s = {4, 7, 8, 9, 4, 2, 4, 2, 4}
print(type(s))
print(len(s))
print(s)

s = set("hello")
print(s)

c = [1, 5, 4, 2, 2, 6, 4]
s = set(c)
print(s)
c = list(s)
print(c)
numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
s = list({x for x in numbers if x % 2 == 0})
print(s)

def to_set(el):
    # st = set(el)
    # return st, len(st)

    return set(el), len(set(el))


print(to_set('я обычная строка'))
print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

t = {'red', 'green', 'blue'}
# print("green" not in t)
for i in t:
    print(i)

# {i for i in последовательность}
# {i for i in последовательность if условие}
# {i(True) if условие else i(False) for i in последовательность}
# {i(True) if условие else i(False) for i in последовательность if условие}


r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
print(a)


