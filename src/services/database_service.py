# src/services/database_service.py

import sqlite3
import os

def connect_to_database():
    database_file = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'inventory.db')
    conn = sqlite3.connect(database_file)
    return conn

# Product related functions

def insert_product(conn, name, description, price, quantity_in_stock):
    """Insert a new product into the database."""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Product (name, description, price, quantity_in_stock) VALUES (?, ?, ?, ?)",
                   (name, description, price, quantity_in_stock))
    conn.commit()

def fetch_all_products(conn):
    """Fetch all products from the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Product")
    return cursor.fetchall()

def update_product(conn, product_id, name, description, price, quantity_in_stock):
    """Update an existing product in the database."""
    cursor = conn.cursor()
    cursor.execute("UPDATE Product SET name=?, description=?, price=?, quantity_in_stock=? WHERE id=?",
                   (name, description, price, quantity_in_stock, product_id))
    conn.commit()

def delete_product(conn, product_id):
    """Delete a product from the database."""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Product WHERE id=?", (product_id,))
    conn.commit()

# User related functions

def insert_user(conn, username, password_hash, role, email):
    """Insert a new user into the database."""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO User (username, password_hash, role, email) VALUES (?, ?, ?, ?)",
                   (username, password_hash, role, email))
    conn.commit()

def fetch_all_users(conn):
    """Fetch all users from the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User")
    return cursor.fetchall()

def update_user(conn, user_id, username, password_hash, role, email):
    """Update an existing user in the database."""
    cursor = conn.cursor()
    cursor.execute("UPDATE User SET username=?, password_hash=?, role=?, email=? WHERE id=?",
                   (username, password_hash, role, email, user_id))
    conn.commit()

def delete_user(conn, user_id):
    """Delete a user from the database."""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM User WHERE id=?", (user_id,))
    conn.commit()

# Category related functions

def insert_category(conn, name, parent_category_id=None):
    """Insert a new category into the database."""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Category (name, parent_category_id) VALUES (?, ?)",
                   (name, parent_category_id))
    conn.commit()

def fetch_all_categories(conn):
    """Fetch all categories from the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Category")
    return cursor.fetchall()

def update_category(conn, category_id, name, parent_category_id=None):
    """Update an existing category in the database."""
    cursor = conn.cursor()
    cursor.execute("UPDATE Category SET name=?, parent_category_id=? WHERE id=?",
                   (name, parent_category_id, category_id))
    conn.commit()

def delete_category(conn, category_id):
    """Delete a category from the database."""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Category WHERE id=?", (category_id,))
    conn.commit()

# Transaction related functions

def insert_transaction(conn, transaction_type, user_id):
    """Insert a new transaction into the database."""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Transaction (transaction_type, user_id) VALUES (?, ?)",
                   (transaction_type, user_id))
    conn.commit()

def fetch_all_transactions(conn):
    """Fetch all transactions from the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Transaction")
    return cursor.fetchall()

def update_transaction(conn, transaction_id, transaction_type, user_id):
    """Update an existing transaction in the database."""
    cursor = conn.cursor()
    cursor.execute("UPDATE Transaction SET transaction_type=?, user_id=? WHERE id=?",
                   (transaction_type, user_id, transaction_id))
    conn.commit()

def delete_transaction(conn, transaction_id):
    """Delete a transaction from the database."""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Transaction WHERE id=?", (transaction_id,))
    conn.commit()

# Additional database functions can be added here
