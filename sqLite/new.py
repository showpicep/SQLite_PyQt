import sqlite3 as sq
import sys
sys.path.append('../')


def Con():
    with sq.connect('chek.db') as con:
        cur = con.cursor()

        #cur.execute("DROP TABLE IF EXISTS cheks")
        cur.execute("""CREATE TABLE IF NOT EXISTS cheks (
            id_check INTEGER PRIMARY KEY AUTOINCREMENT,
            date_check TEXT,
            name_shop TEXT,
            fio TEXT,
            total_value INT
        )
        """)

        #cur.execute("DROP TABLE IF EXISTS products")
        cur.execute("""CREATE TABLE IF NOT EXISTS products (
            id_product INTEGER PRIMARY KEY AUTOINCREMENT,
            cost INT,
            name_product TEXT,
            amount INT
        )
        """)




