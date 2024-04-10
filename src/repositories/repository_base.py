# repository_base.py
import sqlite3
import os

class RepositoryBase:
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'inventory.db')

    @staticmethod
    def get_db_connection():
        return sqlite3.connect(RepositoryBase.DATABASE_PATH)
