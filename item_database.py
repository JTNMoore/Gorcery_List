import sqlite3

def create_database():
    try:
        sqliteConnection = sqlite3.connect('Item_List.db')
        create_table_query = '''CREATE TABLE User_lists (
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
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")