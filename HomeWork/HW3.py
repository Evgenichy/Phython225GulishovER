#  Написать программу калькулятор

# Выберете операцию:
# 1 - 'r' -применяет унарный минус к операнду / Exit
# 2 - "+" -сложение
# 3 - "-" - вычитание
# 4 - "/" - деление
# 5 - "*" - умножение
# 6 - "%" - деление по модулю (остаток от деления)
# 7 - "<" - минимальное из двух чисел
# 8 - ">"- максимальное из двух чисел

print('Выберете операцию:')
uc = input('1. "r" - Exit' '\n2. "+" - сложение' '\n3. "-" - вычитание'
"\n4. '/' - деление" '\n5. "*" - умножение' '\n6. "%" - деление по модулю (остаток от деления)' 
'\n7. "<" - минимальное из двух чисел' '\n8. ">"- максимальное из двух чисел)'
                   '\nВведите номер операции: ')

while True:
    if uc == 'r':
        print("Exit")
        break
    # elif UserChoice != 'r':
    #     print('Net')
    #     break
    # else:
    #     print('ok')

    if uc == 2:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print('Сумма:', a + b)

# if UserChoice == 2:
#     a = int(input('Введите первое число: '))
#     b = int(input('Введите второе число: '))


# i = 0
# while True:
#     n = int(input('Введите номер операции: '))
#     if 2 <= n <= 8:
#         break
#     if n == 1:
#         print('Exit')
#         break
#
# i = m
# res = 0
# while i < w:
#     if n == 2:
#         m = int(input('Введите первое число: '))
#         w = int(input('Введите второе число: '))
#         print(m + w)




# while i > 0:
#     if n == 0:
#         break
#     if n == 2:
#         print()