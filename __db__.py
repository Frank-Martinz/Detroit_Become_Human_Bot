import sqlite3


def create():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS 
        main (user_id INT PRIMARY KEY, name STRING, mission_1 INT,
         mission_2 INT, mission_3 INT, inspect_apartament STRING,
          inspect_table STRING, find_gun STRING, get_gun STRING)""")
    connection.commit()
    connection.close()


def add_new(user_id, name, mission_1, mission_2, mission_3, inspect_apartament, inspect_table, find_gun, get_gun):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    users = list(map(lambda x: x[0], cursor.execute("""SELECT user_id FROM main""").fetchall()))
    if user_id not in users:
        cursor.execute(
            f"""INSERT INTO main VALUES (
            {user_id}, '{name}', {mission_1},
            {mission_2}, {mission_3}, {inspect_apartament},
            {inspect_table}, {find_gun}, {get_gun}
            )""")
    else:
        cursor.execute(f"""UPDATE main SET user_id = {user_id}, name = '{name}', mission_1 = 30, mission_2 = 0, 
                                mission_3 = 0, inspect_apartament = false,
                                inspect_table = false, find_gun = false, get_gun = false
                                WHERE user_id = {user_id};""")
    connection.commit()
    connection.close()


def change(user_id, name, mission_1, mission_2, mission_3, inspect_apartament, inspect_table, find_gun, get_gun):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(
        f"""INSERT OR REPLACE INTO main VALUES (
        {user_id}, '{name}', {mission_1}, {mission_2},
        {mission_3}, {inspect_apartament}, {inspect_table},
        {find_gun}, {get_gun}
        )""")
    connection.commit()
    connection.close()


def get_user(user_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    result = cursor.execute(
        f"SELECT * FROM main WHERE user_id = '{user_id}'"
    ).fetchall()
    return result