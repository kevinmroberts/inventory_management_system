class Transaction:
    def __init__(self, id, transaction_type, timestamp, user_id):
        self.id = id
        self.transaction_type = transaction_type
        self.timestamp = timestamp
        self.user_id = user_id