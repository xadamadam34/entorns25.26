class user:
    def __init__(self, id, username, password, email, idrole, token):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.idrole = idrole
        self.token = token
    
    def __str__(self):
        return f"{self.username} ({self.email}) - Role: {self.idrole}"
