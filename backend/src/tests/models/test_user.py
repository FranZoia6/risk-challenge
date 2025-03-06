import unittest
from src.models.UserModel import User

class TestUserModel(unittest.TestCase):

    def test_user_initialization(self):
        # Creamos una instancia de la clase User
        user = User(1, 'user', 'abc123', 'user user')

        # Verificamos que los atributos se hayan asignado correctamente
        self.assertEqual(user.id, 1)
        self.assertEqual(user.username, 'user')
        self.assertEqual(user.password, 'abc123')
        self.assertEqual(user.fullname, 'user user')

    def test_to_json(self):
        # Creamos una instancia de la clase User
        user = User(1, 'user', 'abc123', 'user user')

        # Llamamos al método `to_json` y verificamos el diccionario resultante
        expected_result = {
            'id': 1,
            'username': 'user',
            'password': 'abc123',
            'fullname': 'user user'
        }
        self.assertEqual(user.to_json(), expected_result)

if __name__ == '__main__':
    unittest.main()
