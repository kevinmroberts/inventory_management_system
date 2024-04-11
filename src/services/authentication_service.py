from src.views.app import App
from src.repositories.user_repository import create_user, validate_user
from tkinter import messagebox

REQUIRED_USERNAME_LENGTH = 4
REQUIRED_PASSWORD_LENGTH = 4

def register_user(username, email, password, confirm_password):
    if username == "" or len(username) < REQUIRED_USERNAME_LENGTH:
        messagebox.showerror("Registration Failed", "Username cannot be blank or less than 4 characters long.")
        return False
    if email == "":
        messagebox.showerror("Registration Failed", "Email cannot be blank.")
        return False
    if password == "" or len(password) < REQUIRED_PASSWORD_LENGTH:
        messagebox.showerror("Registration Failed", "Password cannot be blank or less than 4 characters long.")
        return False
    if password != confirm_password:
        messagebox.showerror("Registration Failed", "Passwords do not match.")
        return False
    else:
        try:
             if create_user(username, email, password):
                return True
        except Exception as e:
            print(f"Registration error: {e}")
            return False

def login(root, username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()

    user = validate_user(username, password)

    if user:
        # Close the login window
        root.destroy()
        # Run main app
        main_app_instance = App()
        main_app_instance.run()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
