class user:
    class user:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

        def __str__(self):
            return f"User(id={self.id}, username='{self.username}', email='{self.email}')"