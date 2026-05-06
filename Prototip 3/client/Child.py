class Child:
    def __init__(self, id, username, password, email, idrole,token):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.idrole = id
        self.token = token
    
    def __str__(self):
        return self.username + ":" + self.password + ":" + self.email