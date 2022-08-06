import sqlite3

def create_connection(db_file):
    sqliteConnection = sqlite3.connect(db_file)
    print("DB Init")

