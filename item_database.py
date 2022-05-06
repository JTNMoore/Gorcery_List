import sqlite3

def create_database():
    try:
        sqliteConnection = open_database()
        create_table_query = '''CREATE TABLE IF NOT EXISTS User_lists (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL);'''
        cursor = sqliteConnection.cursor()
        print("Successfully connected to SQLite")
        cursor.execute(create_table_query)
        sqliteConnection.commit()
        print("SQLite table created")

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        close_database(sqliteConnection)


def open_database():
    sqliteConnection = sqlite3.connect('Item_List.db')
    return sqliteConnection

def close_database(sqliteConnection):
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")


def add_list(name):
    try:
        sqliteConnection = open_database()
        cursor = sqliteConnection.cursor()
        add_table = '''INSERT INTO User_lists (name)
                        VALUES (?);'''
        data_tuple = (name,)
        cursor.execute(add_table, data_tuple)
        print(cursor.lastrowid)
        print("List successfully created in SQLite database.")
    except sqlite3.Error as error:
        print("Failed to insert list into SQLite database", error)
    finally:
        close_database(sqliteConnection)

