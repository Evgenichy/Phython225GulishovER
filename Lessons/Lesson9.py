# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if has_upper and has_lower and has_num:
#         if len(password) >= 8 and has_upper and has_lower and has_num:
#             return True
#         else:
#             if len(password) < 8:
#                 print('Количество символов маленькое')
#     return False
#
#
# p = input('Enter a password: ')
# if check_password(p):
#     print('It`s good password')
# else:
#     print('It`s bad password')


# def get_sum(a=4, b=3, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))
# print(get_sum(c=2))
# s = 2
# print(get_sum(c=s))

# def symbol(elements=20, sign='-'):
#     for i in range(elements):
#         print(sign, end='')
#     print()
#
#
# symbol(10, "+")
# symbol(5, "*")
# symbol(15, "#")
# symbol(7)
# symbol()

# def digits_sum(n, event=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if event and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not event and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print('Сумма четных цифр: ')
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print('Сумма нечетных цифр: ')
# print(digits_sum(9874023, event=False))
# print(digits_sum(38271, event=False))
# print(digits_sum(123456789, event=False))

# def display_info(name, age):
#     print('Name:', name, '\nAge', age)
#
#
# display_info('Ira', 20)
# display_info(age=20, name='Ira')


# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
# print(id(lt1))
# print(id(lt2))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# lt1.pop(1)
# print(lt1)
# print(id(lt1))

# s = 'hello '
# print((id(s)))
# s += 'world'
# print(s)
# print((id(s)))
# # s[1] = 'a'
#
# # st = s[1:2]
# # st = 'a'
# # s = s[:1] + s[1:2] + s[2:]
# s = s[1:-1]
# print(s)
# print((id(s)))
#
# a = 'Hello'
# b = 'Hello'
# print(a == b)
# print(a is b)

# def add_numbers(n):
#     print('In function:', n, '=', id(n))
#     n += 1
#     print('Before:', n, '=', id(n))
#
#
# x = 1
# print(x, '=', id(x))
# add_numbers(x)
# print(x, '=', id(x))

# def add_numbers(n):
#     print('In function:', n, '=', id(n))
#     n += [1]
#     print('Before:', n, '=', id(n))
#
#
# x = [1, 2, 3]
# print(x, '=', id(x))
# add_numbers(x)
# print(x, '=', id(x))

'''
типы данных:
    изменяемые: список (list)
    неизменяемые: число (int), строка (str) вещественное число (float),
булиевые значения (bool)
'''


