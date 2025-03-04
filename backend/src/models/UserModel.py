class User():

    def __init__(self, id, username, password, fullname) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname
    
    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'fullname': self.fullname
        }