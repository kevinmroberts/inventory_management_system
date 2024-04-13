class User:
    def __init__(self, username, email, password, id=None, role='User'):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.role = role
