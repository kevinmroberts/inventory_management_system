# repositories/user_repository.py
from src.repositories.repository_base import RepositoryBase
import hashlib
from tkinter import messagebox

def create_user(username, email, password):
    # Connect to the database
    conn = RepositoryBase.get_db_connection()
    cursor = conn.cursor()

    # Check if the username already exists
    cursor.execute("SELECT * FROM User WHERE username=?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        messagebox.showerror("Registration Failed", "Username already exists. Please choose a different username.")
        return False
    else:
        # Insert the new user into the database
        cursor.execute("INSERT INTO User (username, email, password_hash) VALUES (?, ?, ?)",
                       (username, email, hashlib.sha256(password.encode()).hexdigest()))
        conn.commit()
        messagebox.showinfo("Registration Successful", "User registered successfully.")
        return True
    
    # Close db connection
    conn.close()

def validate_user(username, password):
    # Connect to the database
    conn = RepositoryBase.get_db_connection()
    cursor = conn.cursor()

    # Check if the username and password are valid
    cursor.execute("SELECT * FROM User WHERE username=? AND password_hash=?", (username, hashlib.sha256(password.encode()).hexdigest()))
    user = cursor.fetchone()
    conn.close()

    return user
