import sqlite3 as sq

cars = [
    ('BMW', 54000),
    ('Chevrolet', 46000),
    ('Daewoo', 38000),
    ('Citroen', 29000),
    ('Honda', 33000)
]
con = None
try:
    con = sq.connect("cars.db")
    cur = con.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS cars (
            cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );
        BEGIN;
        INSERT INTO cars VALUES(NULL, 'Renault', 22000);
        UPDATE cars SET price = price + 100;
        """)
    con.commit()
except sq.Error as e:
    if con:
        con.rollback()
    print("Ошибка выполнения запроса")
finally:
    if con:
        con.close()

with sq.connect("cars.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cars (
        cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )
    """)

    cur.executescript("""
    DELETE FROM cars WHERE model LIKE 'B%';
    UPDATE cars SET price = price + 100;
    """)

# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})
# cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
# for car in cars:
#     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)
# cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
# cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
# cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
# cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 95000)")
# cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")

# con.commit() - сохраняет все изменения в базу данных
# con.close() - закрывает соединение с БД


import sqlite3 as sq

# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars (
#         cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     )
#     """)
#
#     cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
#     last_row_id = cur.lastrowid  # lastrowid - возвращает id последней записи
#     buy_car_id = 2
#     cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))

# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars (
#         cars_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     )
#     """)
#
#     cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
#     last_row_id = cur.lastrowid  # lastrowid - возвращает id последней записи
#     buy_car_id = 2
#     cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))