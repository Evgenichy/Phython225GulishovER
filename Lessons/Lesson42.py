import sqlite3 as sq

# with sq.connect('users.db') as con:
#     cur = con.cursor()
    # cur.execute('''
    # CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT '+7 (900)-800-70-60',
    # age INTEGER NOT NULL CHECK(AGE > 0 AND AGE < 100),
    # email TEXT UNIQUE
    # )
    # ''')

    # cur.execute('''
    # ALTER TABLE person
    # RENAME TO person_table
    # ''')

    # cur.execute('''
    #    ALTER TABLE person_table
    #    ADD COLUM address TO home_address
    #    ''')

# with sq.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute('''
#     CREATE TABLE IF NOT EXISTS person(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone BLOB NOT NULL DEFAULT '+7 (900)-800-70-60',
#     age INTEGER NOT NULL CHECK(AGE > 0 AND AGE < 100),
#     email TEXT UNIQUE
#     )
#     ''')
#
#     cur.execute('''
#     INSERT INTO person(email, name, age)
#     VALUES ('dim@mail.ru', 'Дмитрий', '21')
#     ''')


with sq.connect('db_4.db') as con:
    cur = con.cursor()
    cur.execute('''
    SELECT * 
    FROM Ware
    ORDER BY Price DESC
    LIMIT 2, 5;
    ''')


    res = cur.fetchone()
    print(res)
    print()
    res2 = cur.fetchmany(2)
    print(res2)
    # # res = cur.fetchall()
    # # print(res)
    # for res in cur:
    #     print(res)