from tools import database_library

def main():

    db_name = input("What the database should be named?")
    database_library.create_connection(db_name)

if __name__ == "__main__":
    main()


