class Book:
    name = "название книги"
    release = "год выпуска"
    publisher = "издатель"
    genre = "жанр"
    author = "автор"
    price = "цена"

    def print_info(self):
        print(' Электронная библиотека '.center(40, '*'))
        print(f'Имя: {self.name}\n'
              f'Год выпуска: {self.release}\n'
              f'Издатель: {self.publisher}\n'
              f'Жанр: {self.genre}\n'
              f'Автор: {self.author}\n'
              f'Цена: {self.price}')
        print('=' * 40)

    def input_info(self, name, release, publisher, genre, author, price):
        self.name = name
        self.release = release
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_release(self, release):
        self.release = release

    def get_release(self):
        return self.release

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


b1 = Book()
b1.input_info("Изучаем Python", "2019", "Вильямс", "Программирование", "Лутц Марк", "3244.00 Р")
b1.print_info()

b1.set_name('Python. К вершинам мастерства')
print(b1.get_name())

b1.set_release("2016")
print(b1.get_release())

b1.set_publisher("ДМК")
print(b1.get_publisher())

b1.set_genre("Программирование")
print(b1.get_genre())

b1.set_author("Лучано Рамальо")
print(b1.get_author())

b1.set_price("2000.00 Р")
print(b1.get_price())