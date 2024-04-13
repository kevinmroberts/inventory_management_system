from src.repositories.repository_base import RepositoryBase
from src.models.user import User
from src.utils.password_utils import verify_password

class AuthenticationRepository:
    
    @staticmethod
    def register_user(user: User):
        with RepositoryBase.get_db_connection() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO User (username, password_hash, role, email) VALUES (?, ?, ?, ?)",
                    (user.username, user.password, user.role, user.email)
                )
                conn.commit()
                return cursor.lastrowid
            except Exception as e:
                print(f"Error creating user in repository layer: {e}")
                return None
            
    @staticmethod
    def validate_user(user: User):
        with RepositoryBase.get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                # Execute SQL query to fetch the hashed password for the given username
                cursor.execute("SELECT password_hash FROM User WHERE username=?", (user.username,))
                result = cursor.fetchone()
                if result is None:
                    return False, "Could not find username."  # User not found

                stored_password_hash = result[0]
                # Assuming verify_password(stored_hash, provided_password) checks if the passwords match
                if verify_password(stored_password_hash, user.password):
                    return True, ""
                else:
                    return False, "Password was incorrect."
            except Exception as e:
                print(f"Error validating user in repository layer: {e}")
                return False, str(e)