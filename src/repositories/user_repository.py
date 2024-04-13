from src.repositories.repository_base import RepositoryBase
from src.models.user import User
import hashlib

class UserRepository:
    def __init__(self):
        pass

    @staticmethod
    def fetch_user(user: User):
        with RepositoryBase.get_db_connection() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM User WHERE username=?", (user.username,))
                row = cursor.fetchone()  # Use fetchone to get the first row of the results
                if row:
                    # Assuming row contains the fields in the correct order: id, username, password, role, email
                    return User(id=row[0], username=row[1], password=row[2], role=row[3], email=row[4])
            except Exception as e:
                print(f"Error fetching user in repository layer: {e}")
                return None

    
    @staticmethod
    def fetch_users():
        with RepositoryBase.get_db_connection() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM User")
                return [User(id=row[0], username=row[1], password=row[2], role=row[3], email=row[4]) for row in cursor.fetchall()]
            except Exception as e:
                print(f"Error fetching users in repository layer: {e}")

    @staticmethod
    def delete_user(user):
        with RepositoryBase.get_db_connection() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM User WHERE id = ?", (user.id,))
                conn.commit()
            except Exception as e:
                print(f"Error deleting user in repository layer: {e}")

    @staticmethod
    def update_user(user):
        with RepositoryBase.get_db_connection() as conn:
            try:
                cursor = conn.cursor()
                sql = """
                UPDATE User
                SET username = ?, password_hash = ?, role = ?, email = ?
                WHERE id = ?
                """
                cursor.execute(sql, (user.username, user.password_hash, user.role, user.email, user.id))
                conn.commit()
            except Exception as e:
                print(f"Error updating user in repository layer: {e}")



