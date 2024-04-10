class User:
    def __init__(self, id, username, password_hash, role, email):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.role = role
        self.email = email