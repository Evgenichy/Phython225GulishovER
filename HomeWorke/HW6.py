# '''
# первое задание так и не смог понять, использовал все методы списка, которые добавляют элементы в список.
# '''
# # 1
# a = [1, 2, 3]
# b = [11, 12, 13, 4, 2]
# c = []
# d = [4, 2]
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
#     # c.extend(b)
#     # c.append(b)
#     # c.insert(5, 4)
# print(c)
# print()

# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     c.extend(a)
#     i += 1


#1

a = [1, 2, 3]
b = [11, 12, 13, 4, 2]
c = []
if len(b) > len(a):
    for i in range(len(a)):
        c.append(a[i])
        c.append(b[i])
    for i in range(len(a), len(b)):
        c.append(b[i])

print('a =', a)
print('b =', b)
print('c =', c)
print()

# 2
s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
for i in range(len(s)):
    for j in range(len(s)):
        if i != j and s[i] == s[j]:
            break
    else:
        print(s[i], end=' ')
