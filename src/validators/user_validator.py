class UserValidator:

    @staticmethod
    def validate(user):
        if not user.username or not isinstance(user.username, str):
            return False, "Username is required and must be a string."
        if user.password_hash or not isinstance(user.password_hash, str):
            return False, "Password is required and must be a string."
        if user.email or not isinstance(user.email, str):
            return False, "Email is required and must be a string."