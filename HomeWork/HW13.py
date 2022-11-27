# 1
a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
c = {5: 50, 6: 60}
s = a | b | c
print(s)

# 2
q = {
    'emp1': {'name': 'John', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500},
}

print(q['emp3'])
print(q['emp3']['salary'])
print()

q['emp3']['salary'] = 8500

for i in q:
    print(i)
    for j in q[i]:
        print('\t', j, ': ', q[i][j], sep='')

# 3
students = {}
a = int(input('Количество студентов: '))
b = 0
for i in range(a):
    name = input(str(i + 1) + "-й студент: ")
    score = int(input('Балл: '))
    students[name] = score
    b += score
    r = b/a
print('\nСредний балл: ', r)

for j in students:
    if students[j] > r:
        print('\nСтуденты с балом выше среднего: ', j)

#######################################################
# def print_scores(student, *scores):
#     print('Student name: ' + student)
#     for score in scores:
#         print(score)
#
#
# print_scores('Irina', 100, 95, 82, 99, 91)
# print_scores('Igor', 92, 95, 77, 99)
