import tkinter as tk
from tkinter import ttk, messagebox
from src.utils.utils import center_window
from src.services.authentication_service import register_user

def back_to_login(popup, root):
    popup.destroy()  # Close the registration popup
    root.deiconify()  # Re-open the login window

def show_registration_popup(root):
    # Close the login window before showing the registration popup
    root.withdraw()

    popup = tk.Toplevel(root)
    popup.title("Register")
    popup_width = 300
    popup_height = 250
    center_window(popup, popup_width, popup_height)

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
    register_button = ttk.Button(popup, text="Register", style='TButton', command=lambda: attempt_register())
    register_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    # Add a "Back to Login" button
    back_to_login_button = ttk.Button(popup, text="Back to Login", style='TButton', command=lambda: back_to_login(popup, root))
    back_to_login_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    # Ensure the entry fields and button stretch to fill the dialog width
    popup.grid_columnconfigure(1, weight=1)

    # Handle the close event
    def on_popup_close():
        back_to_login(popup, root)
    
    # Handle registering user
    def attempt_register():
        # Extract user input
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        # Attempt to register the user
        registration_successful = register_user(username, email, password, confirm_password)

        # Check if registration was successful
        if registration_successful:
            back_to_login(popup, root)

    popup.protocol("WM_DELETE_WINDOW", on_popup_close)