class User():

    # Constructor que inicializa los atributos del usuario.
    def __init__(self, id, username, password, fullname) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname
    
    # Método que convierte los datos del usuario a un formato JSON.
    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'fullname': self.fullname
        }