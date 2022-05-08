import sqlite3

#this function opens the database connection
def open_database():
    sqliteConnection = sqlite3.connect('Item_List.db')
    return sqliteConnection

#this function closes the database connection
def close_database(sqliteConnection):
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")

#this function deletes the tables in the database and should only be used for testing purposes
def delete_table():
    try:
        #open connection
        sqliteConnection = open_database()
        #delete User_lists table query
        create_table_query = '''DROP TABLE User_lists;'''
        cursor = sqliteConnection.cursor()
        print("Successfully connected to SQLite")
        #execute query
        cursor.execute(create_table_query)
        sqliteConnection.commit()
        print("SQLite table deleted")
        cursor.close()
    #error handling
    except sqlite3.Error as error:
        print("Error while deleting a sqlite table", error)
    finally:
        #close connection
        close_database(sqliteConnection)

def create_database():
    try:
        #open connection
        sqliteConnection = open_database()
        #create User_lists with autoincrementing ID and a unique list name (ignore duplicates)
        create_table_query = '''CREATE TABLE IF NOT EXISTS User_lists (
                                    list_id INTEGER PRIMARY KEY,
                                    list_name TEXT NOT NULL,
                                    UNIQUE (list_name) ON CONFLICT IGNORE);'''
        cursor = sqliteConnection.cursor()
        print("Successfully connected to SQLite")
        #execute query
        cursor.execute(create_table_query)
        sqliteConnection.commit()
        print("SQLite table created")
        cursor.close()
    #error handling
    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        #close connection
        close_database(sqliteConnection)


def add_list(name):
    try:
        #open connection
        sqliteConnection = open_database()
        cursor = sqliteConnection.cursor()
        #create table Item_lists that has autoincrementing itemid, item name, store name, and section name, while referencing the list_id from User_lists
        create_list_table = '''CREATE TABLE IF NOT EXISTS Item_lists (
                                item_id INTEGER PRIMARY KEY,
                                item_name TEXT NOT NULL,
                                store_name TEXT NOT NULL,
                                section_name TEXT NOT NULL,
                                FOREIGN KEY (list_id) REFERENCES User_lists(list_id));'''
        #add list name into User_lists
        add_to_table = '''INSERT INTO User_lists (list_name)
                        VALUES (?);'''
        #list name passed from user
        data_tuple = (name,)
        #execute query
        cursor.execute(add_to_table, data_tuple)
        cursor.execute(create_list_table)
        print("List successfully created in SQLite database.")
        sqliteConnection.commit()
        cursor.close()
    #error handling
    except sqlite3.Error as error:
        print("Failed to insert list into SQLite database", error)
    finally:
        #close connection
        close_database(sqliteConnection)

#this function views all the existing lists in the database
def view_lists():
    try:
        #open connection
        sqliteConnection = open_database()
        cursor = sqliteConnection.cursor()
        #view all lists that exist in User_lists
        view_table = '''SELECT * FROM User_lists;'''
        print("User Lists:")
        #execute query
        cursor.execute(view_table)
        print(cursor.fetchall())
        cursor.close()
    #error handling
    except sqlite3.Error as error:
        print("Failed to retrieve user lists", error)
    finally:
        #close connection
        close_database(sqliteConnection)
