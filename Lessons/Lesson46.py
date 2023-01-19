import sqlite3 as sq


# def read_ava(n):
#     try:
#         with open(f'avatars/{n}.png', 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, 'wb') as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True
#
#
# with sq.connect("cars.db") as con:
#     # con.row_factory = sq.Row
#     print(con.row_factory)
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users (
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     )
#     """)
#
#     cur.execute("SELECT ava FROM users LIMIT 1")
#     img = cur.fetchone()['ava']
#
#     write_ava('out.png', img)
#
#     img = read_ava(1)
#     if img:
#         binary = sq.Binary(img)
#         cur.execute("INSERT INTO users VALUES ('Илья', ?, 1000)", (binary,))
#
#     cur.execute('SELECT model, price FROM cars')
#
#     # rows = cur.fetchall()
#     # rows = cur.fetchone()
#     # rows = cur.fetchmany(5)
#     for res in cur:
#         print(res['model'], res['price'])

#########
# with sq.connect("cars.db") as con:
#     cur = con.cursor()

    # with open('sql_dump.sql', 'w') as f:
    #     for sql in con.iterdump():
    #         f.write(sql)

    # with open('sql_dump.sql', 'r') as f:
    #     sql = f.read()
    #     cur.executescript(sql)




