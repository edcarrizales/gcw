import sqlite3
import mysql.connector

from MySQLDatabase import MySQLDatabase
from SQLiteDatabase import SQLiteDatabase


class DatabaseHandler:

    def __init__(self, database_type, **kwargs):
        if database_type == 'mysql':
            self.db_handler = MySQLDatabase(**kwargs)
        elif database_type == 'sql_lite':
            self.db_handler = SQLiteDatabase(**kwargs)
        else:
            raise ValueError("Tipo de base de datos no válido. Utiliza 'mysql' o 'sqlite'.")

    def create_table(self, table_name, columns):
        self.db_handler.create_table(table_name, columns)

    def select(self, table_name, columns="*", condition=None):
        return self.db_handler.select(table_name, columns, condition)

    def insert(self, table_name, data):
        self.db_handler.insert(table_name, data)

    def update(self, table_name, data, condition):
        self.db_handler.update(table_name, data, condition)

    def delete(self, table_name, condition):
        self.db_handler.delete(table_name, condition)

    def close_connection(self):
        self.db_handler.close_connection()