import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import hashlib
from src.services.database_service import connect_to_database
from src.gui_components.main_app import MainApp
from src.utils.utils import center_window

def login(root, username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()

    # Connect to the database
    conn = connect_to_database()
    cursor = conn.cursor()

    # Check if the username and password are valid
    cursor.execute("SELECT * FROM User WHERE username=? AND password_hash=?", (username, hashlib.sha256(password.encode()).hexdigest()))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        # Close the database connection
        conn.close()
        # Close the login window
        root.destroy()
        # Run main app
        main_app_instance = MainApp()
        main_app_instance.run()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
        # Close the database connection
        conn.close()

def back_to_login(popup, root):
    popup.destroy()  # Close the registration popup
    root.deiconify()  # Re-open the login window

def register_user(username_entry, email_entry, password_entry, confirm_password_entry, popup, root):
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if password != confirm_password:
        messagebox.showerror("Registration Failed", "Passwords do not match.")
        return

    # Connect to the database
    conn = connect_to_database()
    cursor = conn.cursor()

    # Check if the username already exists
    cursor.execute("SELECT * FROM User WHERE username=?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        messagebox.showerror("Registration Failed", "Username already exists. Please choose a different username.")
    else:
        # Insert the new user into the database
        cursor.execute("INSERT INTO User (username, email, password_hash) VALUES (?, ?, ?)",
                       (username, email, hashlib.sha256(password.encode()).hexdigest()))
        conn.commit()
        messagebox.showinfo("Registration Successful", "User registered successfully.")
        back_to_login(popup, root)

    # Close the database connection
    conn.close()

def show_registration_popup(root):
    # Close the login window before showing the registration popup
    root.withdraw()

    popup = tk.Toplevel(root)
    popup.title("Register")
    popup_width = 300
    popup_height = 250
    center_window(popup, popup_width, popup_height)

    style = ttk.Style()
    style.configure('TButton', font=('Segoe UI', 10), borderwidth='4')
    style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])

    # Applying consistent styling
    popup.configure(bg='white')  # Set background color

    style = ttk.Style()
    style.configure('TButton', font=('Segoe UI', 10), borderwidth='4')
    style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])

    # Labels and entry fields with consistent styling and spacing
    username_label = tk.Label(popup, text="Username:", font=('Segoe UI', 10), bg='white')
    username_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    username_entry = tk.Entry(popup, font=('Segoe UI', 10))
    username_entry.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    email_label = tk.Label(popup, text="Email:", font=('Segoe UI', 10), bg='white')
    email_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    email_entry = tk.Entry(popup, font=('Segoe UI', 10))
    email_entry.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

    password_label = tk.Label(popup, text="Password:", font=('Segoe UI', 10), bg='white')
    password_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    password_entry = tk.Entry(popup, show="*", font=('Segoe UI', 10))
    password_entry.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

    confirm_password_label = tk.Label(popup, text="Confirm Password:", font=('Segoe UI', 10), bg='white')
    confirm_password_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    confirm_password_entry = tk.Entry(popup, show="*", font=('Segoe UI', 10))
    confirm_password_entry.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

    # Adjust the button styling and placement
    register_button = ttk.Button(popup, text="Register", style='TButton', command=lambda: register_user(username_entry, email_entry, password_entry, confirm_password_entry, popup, root))
    register_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    # Add a "Back to Login" button
    back_to_login_button = ttk.Button(popup, text="Back to Login", style='TButton', command=lambda: back_to_login(popup, root))
    back_to_login_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    # Ensure the entry fields and button stretch to fill the dialog width
    popup.grid_columnconfigure(1, weight=1)

    # Handle the close event
    def on_popup_close():
        root.destroy()

    popup.protocol("WM_DELETE_WINDOW", on_popup_close)

def main():
    root = tk.Tk()
    root.title("Login")
    width = 300
    height = 250
    center_window(root, width, height)  # Adjust size as needed

    style = ttk.Style()
    style.configure('TButton', font=('Segoe UI', 10), borderwidth='4')
    style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])

    # Username
    username_label = tk.Label(root, text="Username:", font=('Segoe UI', 10))
    username_label.pack()
    username_entry = tk.Entry(root, font=('Segoe UI', 10))
    username_entry.pack(pady=(0, 10))

    # Password
    password_label = tk.Label(root, text="Password:", font=('Segoe UI', 10))
    password_label.pack()
    password_entry = tk.Entry(root, show="*", font=('Segoe UI', 10))
    password_entry.pack(pady=(0, 20))

    # Login Button
    login_button = ttk.Button(root, text="Login", style='TButton', command=lambda: login(root, username_entry, password_entry))
    login_button.pack(ipadx=10, ipady=5)

    # Register Button
    register_button = ttk.Button(root, text="Register", style='TButton', command=lambda: show_registration_popup(root))
    register_button.pack(ipadx=10, ipady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
