import sqlite3

def create_connection():
    sqlite_connection = sqlite3.connect("database.db")
    cursor = sqlite_connection.cursor()
    print("DB Init")

#def make_tables(table_name):

