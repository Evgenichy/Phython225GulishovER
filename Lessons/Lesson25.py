class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, num, surname, percent, value=0):
        self.num = num
        self.surname = surname
        self.percent = percent
        self.value = value
        print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт')

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def edit_owner(self, surname):
        self.surname = surname

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счета: {eur_val} {Account.suffix_eur}')

    def print_balance(self):
        print(f'Текущий баланс: {self.value} {Account.suffix}')

    def print_info(self):
        print(f'Информация о счете:')
        print('-' * 20)
        print(f'#{self.num}')
        print(f'Владелец: {self.surname}')
        #print(f'Текущий баланс: {self.value}')
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')
        print('-' * 20)

    def add_percents(self):
        self.value += self.value * self.percent
        print('Проценты успешно начислены')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f'Нищеброд, у тебя нет {val} {Account.suffix}')
        else:
            self.value -= val
            print(f'{val} {Account.suffix} было успешно снято!')
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f'{val} {Account.suffix} было успешно добавленно!')
        self.print_balance()


acc = Account('12345', 'Долгих', 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
Account.set_usd_rate(2)
acc.convert_to_usd()

Account.set_eur_rate(3)
acc.convert_to_eur()
print()

acc.edit_owner('Дюма')
acc.print_info()
print()

acc.add_percents()
print()

acc.withdraw_money(1000)
print()

acc.add_money(5000)
print()

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.veryfi_weight(weight)
#
#         self.__fio = fio.split()
#         self.__old = old
#         self.__passport = ps
#         self.__weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError('ФИО должно быть строкой')
#         f = fio.split()
#         print(f)
#         if len(f) != 3:
#             raise TypeError('Неверный формат ФИО')
#         letters = ''.join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         print(letters)
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError('В ФИО можно использовать только буквы и дефис')
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError('Возраст должен быть числом в диапазоне от 14 до 120 лет')
#
#     @classmethod
#     def veryfi_weight(cls, w):
#         if not isinstance(w,float) or w < 20:
#             raise TypeError('Вес должен быть вещественным числом от 20 до 120 кг')
#
#
# p1 = UserData('Самосвал Камаз Уралович', 26, '7423 008976', 78.2)

# Продолжение в Lesson 26
