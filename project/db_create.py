import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect('flasktaskr.db') as connection:

    c = connection.cursor()

    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL,
                status INTEGER NOT NULL)""")

    # insert dummy data into table
    c.execute("""INSERT INTO tasks (name, due_date, priority, status)
                VALUES("FINISH this tutorial", "03/25/2015", 10, 1)""")

    c.execute("""INSERT INTO tasks (name, due_date, priority, status)
                VALUES("FINISH REAL PYTHON COURSE 2", "02/25/2015", 10, 1)""")


