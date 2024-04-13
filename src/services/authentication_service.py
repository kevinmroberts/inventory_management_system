from src.views.app import App
from src.repositories.authentication_repository import AuthenticationRepository
from src.repositories.user_repository import UserRepository
from src.models.user import User
from tkinter import messagebox
from src.utils.password_utils import hash_password

REQUIRED_USERNAME_LENGTH = 4
REQUIRED_PASSWORD_LENGTH = 4

class AuthenticationService:

    def __init__(self, event_manager):
        self.event_manager = event_manager

    def register_user(self, user: User):
        if UserRepository.fetch_user(user) != None:
            messagebox.showerror("Registration Failed", "Username already exists. Please choose a new username.")
            return False
        if user.username == "" or len(user.username) < REQUIRED_USERNAME_LENGTH:
            messagebox.showerror("Registration Failed", "Username cannot be blank or less than 4 characters long.")
            return False
        if user.email == "":
            messagebox.showerror("Registration Failed", "Email cannot be blank.")
            return False
        if user.password == "" or len(user.password) < REQUIRED_PASSWORD_LENGTH:
            messagebox.showerror("Registration Failed", "Password cannot be blank or less than 4 characters long.")
            return False
        else:
            user.password = hash_password(user.password)
            try:
                if AuthenticationRepository.register_user(user):
                    return True
            except Exception as e:
                print(f"Registration error: {e}")
                return False

    def login(self, root, user: User):
        isValid, error_message = AuthenticationRepository.validate_user(user)

        if isValid:
            # Close the login window
            root.destroy()
            # Run main app
            main_app_instance = App()
            main_app_instance.run()
        else:
            messagebox.showerror("Login Failed", error_message)
