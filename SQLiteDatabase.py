import sqlite3


class SQLiteDatabase:

    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        # Example columns format: "id INTEGER PRIMARY KEY, name TEXT, age INTEGER"
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.connection.commit()

    def select(self, table_name, columns="*", condition=None):
        query = f"SELECT {columns} FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self, table_name, data):
        # Example data format: {"name": "John", "age": 25}
        columns = ", ".join(data.keys())
        values = ", ".join(f'"{value}"' for value in data.values())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.cursor.execute(query)
        self.connection.commit()

    def update(self, table_name, data, condition):
        # Example data format: {"age": 26}
        set_clause = ", ".join(f'{key} = "{value}"' for key, value in data.items())
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()