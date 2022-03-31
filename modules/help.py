import sqlite3 as sq


def Below400():
    with sq.connect('C:/Users/Acer/Desktop/Chek/sqLite/chek.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM cheks WHERE total_value < 400")
        tmp = cur.fetchall()
        result = list(tmp[0])

        print(result)
        return result


def Above400():
    with sq.connect('C:/Users/Acer/Desktop/Chek/sqLite/chek.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM cheks WHERE total_value > 400")
        tmp = cur.fetchall()
        result = list(tmp[1])
    return result


def GetStringOfRequest():
    result = Above400()
    nwe = Below400()
    tmp = ['Номер чека:', 'Дата получения:', 'Магазин:', 'ФИО:', 'Общая стоимость:']
    res = {}

    for idx, value in enumerate(tmp):
        res[value] = nwe[idx]

    return res
