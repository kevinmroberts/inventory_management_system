from src.gui.app import App
from src.repositories.user_repository import create_user, validate_user
from tkinter import messagebox

def register_user(username_entry, email_entry, password_entry, confirm_password_entry):
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if password != confirm_password:
        messagebox.showerror("Registration Failed", "Passwords do not match.")
        return
    else:
        create_user(username, email, password)

def login(root, username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()

    user = validate_user(username, password)

    if user:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        # Close the login window
        root.destroy()
        # Run main app
        main_app_instance = App()
        main_app_instance.run()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
