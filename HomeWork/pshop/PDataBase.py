import sqlite3
import time
import math


class PDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = '''
                SELECT * 
                FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Ошибка чтения из базы данных ')
        return []

    def add_goods(self, title, text, url):
        try:
            self.__cur.execute("SELECT COUNT() as 'count' FROM goods WHERE url LIKE ?", (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('Товар с таким url уже существует ')
                return False
            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO goods VALUES(NULL, ?, ?, ?, ?)', (title, text, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления товара в БД ' + str(e))
            return False

        return True

    def get_goods_announce(self):
        try:
            self.__cur.execute("SELECT id, title, text, url FROM goods ORDER BY time")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка получения товара из БД ' + str(e))
        return []

    # def get_goods(self, alias):
    #     try:
    #         self.__cur.execute(f'SELECT title, text FROM posts WHERE id={alias} LIMIT 1')
    #         res = self.__cur.fetchone()
    #         if res:
    #             return res
    #     except sqlite3.Error as e:
    #         print('Ошибка получения товара из БД' + str(e))
    #
    #     return False, False
