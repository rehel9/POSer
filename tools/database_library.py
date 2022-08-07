import sqlite3
from product import Product

connect = sqlite3.connect("products.db")
cursor = connect.cursor()
print("DB Init")

cursor.execute("""CREATE TABLE Productos (
                    id INTEGER,
                    name TEXT,
                    quantity INTEGER, 
                    price REAL
                     )""")

prod_1 = Product(1, "Maple", 1, 50.5)
def insert_product(prod):
    with connect:
        cursor.execute("INSERT INTO Productos VALUES (:id, :name, :quantity, :price)", {"id": prod.first,
                                                                                    "name": prod.name,
                                                                                    "quantity": prod.quantity,
                                                                                    "price": prod.price})

def delete_product(prod):
    with connect:
        cursor.execute("DELETE from Productos WHERE id = :id AND name = :name",
                       {"id": prod.id, "name": prod.name})

connect.commit()



connect.close()