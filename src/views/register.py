import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.utils.utils import center_window
from src.services.authentication_service import AuthenticationService
from src.models.user import User
from src.utils.singleton import Singleton
from src.utils.event_manager import EventManager

class RegisterForm(Singleton):
    initialized = False

    def __init__(self, root):
        self.root = root
        if not self.initialized:
            self.init_ui()
            self.initialized = True
            self.event_manager = EventManager()

    def show(self):
        """Display the registration form and withdraw the login form."""
        self.root.withdraw()
        self.popup.deiconify()
        self.initialized = False

    def init_ui(self):
        """Initialize the UI components of the registration form."""
        self.popup = tk.Toplevel(self.root)
        self.popup.title("Register")
        popup_width = 300
        popup_height = 250
        center_window(self.popup, popup_width, popup_height)
        self.popup.configure(bg='white')
        self.setup_widgets()
        self.popup.protocol("WM_DELETE_WINDOW", self.back_to_login)

    def setup_widgets(self):
        """Set up widgets for the registration form."""
        style = ttk.Style()
        style.configure('TButton', font=('Segoe UI', 10), borderwidth='4')
        style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])

        # Define and place widgets
        username_label = tk.Label(self.popup, text="Username:", font=('Segoe UI', 10), bg='white')
        username_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.username_entry = tk.Entry(self.popup, font=('Segoe UI', 10))
        self.username_entry.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

        email_label = tk.Label(self.popup, text="Email:", font=('Segoe UI', 10), bg='white')
        email_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.email_entry = tk.Entry(self.popup, font=('Segoe UI', 10))
        self.email_entry.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

        password_label = tk.Label(self.popup, text="Password:", font=('Segoe UI', 10), bg='white')
        password_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.password_entry = tk.Entry(self.popup, show="*", font=('Segoe UI', 10))
        self.password_entry.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

        confirm_password_label = tk.Label(self.popup, text="Confirm Password:", font=('Segoe UI', 10), bg='white')
        confirm_password_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.confirm_password_entry = tk.Entry(self.popup, show="*", font=('Segoe UI', 10))
        self.confirm_password_entry.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

        register_button = ttk.Button(self.popup, text="Register", style='TButton', command=self.attempt_register)
        register_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        back_to_login_button = ttk.Button(self.popup, text="Back to Login", style='TButton', command=self.back_to_login)
        back_to_login_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.popup.grid_columnconfigure(1, weight=1)
        self.popup.protocol("WM_DELETE_WINDOW", self.back_to_login)

    def back_to_login(self):
        """Close the registration popup and reopen the login window."""
        self.popup.destroy()
        self.root.deiconify()

    def attempt_register(self):
        """Attempt to register the user with the provided credentials."""
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Registration Failed", "Please make sure both of your passwords match.")
        else:
            auth_service = AuthenticationService(self.event_manager)
            registration_successful = auth_service.register_user(User(username=username, email=email, password=password))

            if registration_successful:
                messagebox.showinfo("Registration Successful", "You have been registered successfully.")
                self.back_to_login()

def show_registration_popup(root):
    """Function to show the registration popup, ensuring singleton pattern."""
    RegisterForm(root)
