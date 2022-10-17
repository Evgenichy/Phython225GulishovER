# a = 1
# b = 2
# print('a:', a)
# print('b:', b)
# a = a + b  # a = 1 + 2 = 3
# b = a - b  # b = 3 - 2 = 1
# a = a - b  # a = 3 - 1 = 2
# print('a:', a)
# print('b:', b)

#  Функуии преобрпзования типов
#  int() - числовой тип
#  str() - строковый тип
#  float() - вещественый тип
#  bool() - булиевый тип

# num1 = '2'
# num2 = 3
# # res = int(num1) + num2
# res = num1 + str(num2)
# print(res)
# print(type(res))

# print(int(3.8))
# print(round(3.895, 2))

# a = '5.2'
# b = 10
# c = float(a) + b
# print(c)
# print(type(c))


# name = 'Evgenichy'
# age = 23
# print('Меня зовут ', name, '. Мне ', age, ' года.')
# print('Меня зовут ' + name + '. Мне ' + str(age) + ' года.')
# print('Меня зовут ', name, '. Мне ', age, ' года.', sep='', end=' \n')
# print('Я учу Python')

# num = int(input('Введите число: '))
# power = int(input('Введите степень: '))
# res = num ** power
# print('Число', num, 'в степень', power, 'равно:', res)

# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)
# print(type(b1))

# print(bool('python'))
# print(bool(''))  # False - при пустой строке и 0
# print(bool(' '))  # True - с любым символом
# print(bool(-15.2))
# print(bool(0))
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(type(test))
# test = 5
# print(test)
# print(type(test))

# print(7 == 7)
# print(7 + 2 == 7)
# print(7 + 2 != 7)
# print(8 > 5)
# print(8 < 5)
# print('привет' > 'Привет')

# print(2 < 14 < 9)
# print(2 * 5 > 7 >= 4 + 3)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True : False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False : True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False : False)

# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True : False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False : True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False : False)

# print(not 9 - 5)
# print(not 5 - 5)

# cnt = 5
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input('Введите свой возраст: '))
# if age >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')

# a = 15
# b = 5
# if a > b:
#     print('a > b')
# elif a < b:
#     print('b > a')
# else:
#     print('a == b')

# a = int(input('Введите длину стороны треугольника: '))
# b = int(input('Введите длину стороны треугольника: '))
# c = int(input('Введите длину стороны треугольника: '))
#
# if a == b == c:
#     print('Треугольнк равностороний')
# elif a == b or a == c or b == c:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольнк разностороний')

# day = int(input('Введите день недели (цифрой): '))
# if 1 <= day <= 5: # (day >= 1) and (day <= 5):
#     print('Рабочий день - ', end='')
# elif day == 6 or day == 7:
#     print('Выходной день - ', end='')
# else:
#     print('Такого дня недели не существует')

# day = int(input('Введите день недели (цифрой): '))
# if 1 <= day <= 5:
#     print('Рабочий день - ', end='')
#     if day ==1:
#         print('понедельник')
#     if day ==2:
#         print('вторник')
#     if day ==3:
#         print('среда')
#     if day ==4:
#         print('четверг')
#     if day ==5:
#         print('пятница')
# elif day == 6 or day == 7:
#     print('Выходной день - ', end='')
#     if day == 6:
#             print('суббота')
#     if day == 7:
#             print('воскресение')
# else:
#     print('Такого дня недели не существует')


# month = int(input('введите порядковый номер месяца: '))
# if 1 <= month <= 12:
#     print('месяц - ', end='')
#     if month == 1:
#         print('январь')
#     if month == 2:
#         print('февраль')
#     if month == 3:
#         print('март')
#     if month == 4:
#         print('апрель')
#     if month == 5:
#         print('май')
#     if month == 6:
#         print('июнь')
#     if month == 7:
#         print('июль')
#     if month == 8:
#         print('август')
#     if month == 9:
#         print('сентябрь')
#     if month == 10:
#         print('октябрь')
#     if month == 11:
#         print('ноябрь')
#     if month == 12:
#         print('декабрь')
# else:
#     print('такого месяца нет')


# n = int(input('Введите кол-во ворон: '))
# if 0 <= n <= 9:
#     if n == 1:
#         print("На ветке", n, 'Ворона')
#     if 2 <= n <= 4:
#         print("На ветке", n, 'Вороны')
#     else:
#         print('На ветке', n, 'ворон')
# else:
#     print("Ошибка ввода данных")
