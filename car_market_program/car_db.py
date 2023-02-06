import _sqlite3
import sqlite3


class MyDb:
    with sqlite3.connect("cars.db") as db:
        curs = db.cursor()
        # curs.execute("DROP TABLE cars_db")
        create_db = """CREATE TABLE IF NOT EXISTS cars_db (
        id integer PRIMARY KEY,
        seller text,
        mark text,
        model texty,
        price integer,
        year integer
        )"""
        curs.execute(create_db)
