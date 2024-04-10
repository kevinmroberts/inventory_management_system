import tkinter as tk
from tkinter import ttk
from src.utils.utils import center_window
from src.services.authentication_service import login
from src.gui.register import show_registration_popup

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
    username_label = ttk.Label(root, text="Username:", font=('Segoe UI', 10))
    username_label.pack()
    username_entry = tk.Entry(root, font=('Segoe UI', 10))
    username_entry.pack(pady=(0, 10))

    # Password
    password_label = ttk.Label(root, text="Password:", font=('Segoe UI', 10))
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
