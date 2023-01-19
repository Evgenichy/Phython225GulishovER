import sqlite3 as sq

#tools_store

tools =[
    ('Шуруповерт', 7990),
    ('Угловая шлифовальная машинка', 6180),
    ('Гайковерт', 11560),
    ('Гравер', 1540),
    ('Дрель', 7560),
    ('Компрессор', 12380),
    ('Краскопульт', 2980),
    ('Лобзик электрический', 3550),
    ('Перфоратор', 7150),
    ('Пила электричесая', 5780),
]

with sq.connect("tools_store.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS tools (
        tools_id INTEGER PRIMARY KEY AUTOINCREMENT,
            tools TEXT,
            price INTEGER
    )
    """)

    for ts in tools:
        cur.execute("INSERT INTO tools VALUES(NULL, ?, ?)", ts)
