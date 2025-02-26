import sqlite3
import os


class CustomerDB:
    def __init__(self, db_path="data/customers.db"):
        self.db_path = os.path.abspath(db_path)
        self.connection = None

    def connect(self):
        if self.connection is None:
            if not os.path.exists(self.db_path):
                raise FileNotFoundError(f"Файл базы данных не найден: {self.db_path}")
            self.connection = sqlite3.connect(self.db_path)

    def get_customer_from_db(self):
        self.connect()
        cursor = self.connection.cursor()
        query = ("SELECT email, first_name, last_name, address, "
                 "city, country, state, phone FROM customers LIMIT 1;")
        cursor.execute(query)
        row = cursor.fetchone()
        self.connection.close()

        if row:
            return {
                "email": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "address": row[3],
                "city": row[4],
                "country": row[5],
                "state": row[6],
                "phone": row[7],
            }
        else:
            return None
