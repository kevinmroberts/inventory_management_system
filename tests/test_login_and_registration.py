import unittest
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.scripts.gui_login import login, register_user

class TestLoginAndRegistration(unittest.TestCase):
    def test_login_success(self):
        # Mocking connect_to_database function
        with patch("src.services.database_service.connect_to_database") as mock_connect:
            # Mocking database cursor and execute method
            mock_cursor = mock_connect.return_value.cursor.return_value
            mock_cursor.fetchone.return_value = (1, "username", "hashed_password")

            # Calling login function with valid username and password
            result = login("username", "password")

            # Asserting login success message
            self.assertEqual(result, "Login Successful")

    def test_login_failure(self):
        # Mocking connect_to_database function
        with patch("src.services.database_service.connect_to_database") as mock_connect:
            # Mocking database cursor and execute method
            mock_cursor = mock_connect.return_value.cursor.return_value
            mock_cursor.fetchone.return_value = None

            # Calling login function with invalid username and password
            result = login("invalid_username", "invalid_password")

            # Asserting login failure message
            self.assertEqual(result, "Login Failed")

    def test_register_user_success(self):
        # Mocking connect_to_database function
        with patch("src.services.database_service.connect_to_database") as mock_connect:
            # Mocking database cursor and execute method
            mock_cursor = mock_connect.return_value.cursor.return_value
            mock_cursor.fetchone.return_value = None

            # Calling register_user function with new username and password
            result = register_user("new_username", "new_password")

            # Asserting registration success message
            self.assertEqual(result, "Registration Successful")

    def test_register_user_failure(self):
        # Mocking connect_to_database function
        with patch("src.services.database_service.connect_to_database") as mock_connect:
            # Mocking database cursor and execute method
            mock_cursor = mock_connect.return_value.cursor.return_value
            mock_cursor.fetchone.return_value = (1, "existing_username", "hashed_password")

            # Calling register_user function with existing username
            result = register_user("existing_username", "new_password")

            # Asserting registration failure message
            self.assertEqual(result, "Registration Failed")

if __name__ == "__main__":
    unittest.main()
