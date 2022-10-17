# a = [7, 9, 2, 1, 17]
# # a[0], a[4] = a[4], a[0] - обращение по индексу
# a[0], a[-1] = a[-1], a[0]
# print(a)

# Срез
# Список[start:stop:step]

# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::2])
# print(s[::-1])
# # print(s[1:5:-1]) будет пустой список - []
# print(s[5:1:-1])
# # print(s[6]) - error
# print(s[3:7])

# a = [1,2,3,4,5,6,7]
# print(a[:])
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[:1])
# print(a[-1:])
# print(a[3:4])
# print(a[4:])
# print(a[4:1:-1])
# print(a[4:1:-1])
# print(a[2:5])

# s = [5, 9, 3, 7, 1, 8]
# s[1:3] = [0, 0, 0, 0]
# print(s)
# # s[1:2] = [20]
# s[2] = 20
# # s[-1:] = [8, 8, 8, 8]
# s[8:] = [9, 8, 8, 8]
# print(s)

# Методы списков

# s = [5, 9, 3, 7, 1, 8]
# s.append(99)  # добавляет один элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(1, 100)  # добавляет элемент по индексу(первый праметр), с заданным значением (второй параметр)
# print(s)

# s = []
# n = int(input('n = '))
# for num in range(n):
#     x = int(input('-> '))
#     s.append(x)
# print(s)

# s = []
# n = int(input('n = '))
# for num in range(n):
#     x = int(input('-> '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, 'не делится на 3')
# print(s)

# a = [5, 9, 2, 1, 4, 3]  #на заметку
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11,12, 13]
# c = []
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print(c)

# s = [5, 9, 3, 7, 1, 8]
# s.remove(9)  # удаляет первый искомый элемент
# print(s)
# last = s.pop() # без параметров - удаляет поседний элемен списка
# print(last)
# print(s)
# s.clear()  #удаляет из списка все элементы
# del s - удаляет сам список
# del s[2] - удаляет по заданому индексу

# s = [int(input('-> ')) for i in range(int(input('n = ')))]
# k = int(input('Enter index: '))
# s.pop(k)
# print(s)


# s = [5, 9, 3, 7, 1, 8, 9, 9, 9, 9]
# num = s.count(9)  # количество заданных значений в списке
# print(num)
# print(s)
# ind = s.index(3)
# print(ind)


# a = [1, 2, 3]
# b = a
# print('a =', a)
# print('b =', b)
# a.append(20)
# print('a =', a)
# print('b =', b)


# s = [5, 9, 3, 7, 1, 8, 9, 9, 9, 9]
# print(s)
# s.reverse()  # переворачивает список
# print(s)
# s.sort()  # сортирует в порядке возрастания, изменяет список. reverse=True - сортировка по убыванию
# print(s)
# a = sorted(s)   # сортирует в порядке возрастания, НЕ изменяет список
# a = sorted(s, reverse=True)
# print(a)

# s2 = ['Виталий', 'Сергей', 'Александр', 'Анна']
# s2.sort(key=len, reverse=True)
# print(s2)

