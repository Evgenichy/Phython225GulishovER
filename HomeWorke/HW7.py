#  1
import random as r


m = [[r.randint(-20, 11) for x in range(3)] for y in range(4)]
n = 0
for row in m:
    for x in row:
        if x < 0:
            n += 1
        print(x, end='\t\t')
    print()

print('Количество отрицательных элементов:', n)

print()
#  2

m = [[r.randint(0, 5) for x in range(3)] for y in range(4)]
n = 1
for row in m:
    for x in row:
        if x > 0:
            n *= x
        print(x, end='\t\t')
    print()

print('Произведение не нулевых элементов:', n)

