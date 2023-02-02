n = [int(input('-> ')) for i in range(int(input('Элементов списка: ')))]
for i in range(len(n)):
    if i % 2 == 0:
        print(n[i], end=' ')

print()
n = [int(input('-> ')) for i in range(int(input('Элементов списка: ')))]
for i in range(1, len(n)):
    if n[i] > n[i - 1]:
        print(n[i], end=' ')
