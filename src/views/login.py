import tkinter as tk
from tkinter import ttk
from src.utils.utils import center_window
from src.services.authentication_service import AuthenticationService
from src.views.register import RegisterForm
from src.models.user import User
from src.utils.singleton import Singleton
from src.utils.event_manager import EventManager

class Login(Singleton):
    def __init__(self):
        if not hasattr(self, 'initialized') or not self.initialized:
            self.root = tk.Tk()
            self.root.title("Login")
            self.event_manager = EventManager()
            self.authentication_service = AuthenticationService(self.event_manager)
            self.setup_gui()
            self.initialized = True

    def setup_gui(self):
        """Sets up the login GUI."""
        width = 300
        height = 250
        center_window(self.root, width, height)

        style = ttk.Style()
        style.configure('TButton', font=('Segoe UI', 10), borderwidth='4')
        style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])

        username_label = ttk.Label(self.root, text="Username:", font=('Segoe UI', 10))
        username_label.pack()
        self.username_entry = tk.Entry(self.root, font=('Segoe UI', 10))  # Make it accessible as self.username_entry
        self.username_entry.pack(pady=(0, 10))

        password_label = ttk.Label(self.root, text="Password:", font=('Segoe UI', 10))
        password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*", font=('Segoe UI', 10))  # Make it accessible as self.password_entry
        self.password_entry.pack(pady=(0, 20))

        login_button = ttk.Button(self.root, text="Login", style='TButton', 
                                command=self.on_login_click)
        login_button.pack(ipadx=10, ipady=5)

        register_button = ttk.Button(self.root, text="Register", style='TButton', 
                                    command=lambda: RegisterForm(self.root).show())
        register_button.pack(ipadx=10, ipady=5)

    def on_login_click(self):
        """Handler for login button click."""
        # Capture the username and password from the entries
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Create a User object or pass these directly to your authentication service
        user = User(username=username, password=password, email="")  # Assuming email is optional or to be fetched elsewhere

        # TODO: Figure out why after logging in, the main app window popup twice.
        # Logins the user using Authentication Server
        self.authentication_service.login(self.root, user)

    def run(self):
        self.root.mainloop()

