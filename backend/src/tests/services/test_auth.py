from unittest.mock import patch, MagicMock
import unittest
from src.services.AuthService import AuthService
from src.models.UserModel import User

class TestAuthService(unittest.TestCase):

    @patch('src.services.AuthService.get_connection')  
    def test_login_user_success(self, mock_get_connection):
        mock_connection = MagicMock()
        mock_get_connection.return_value = mock_connection
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.fetchone.return_value = (1, 'username', 'password')

        user = MagicMock()
        user.username = 'username'
        user.password = 'password'

        result = AuthService.login_user(user)
        
        # Verificamos si el resultado es un objeto de tipo User
        self.assertIsInstance(result, User)
        
        # Verificamos que se haya llamado a la función `fetchone`
        mock_cursor.fetchone.assert_called_once()

        # Verificamos que el resultado sea correcto
        self.assertEqual(result.id, 1)
        self.assertEqual(result.username, 'username')

    @patch('src.services.AuthService.get_connection')  
    def test_add_user_success(self, mock_get_connection):
        mock_connection = MagicMock()
        mock_get_connection.return_value = mock_connection
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
        mock_cursor.execute.return_value = None  

        user = MagicMock()
        user.username = 'new_user'
        user.password = 'password'
        user.fullname = 'Full Name'

        result = AuthService.add_user(user)
        
        # Verificamos que el mensaje devuelto es el esperado
        self.assertEqual(result,(True, 'User added successfully'))

        # Verificamos que se haya llamado al método `execute` del cursor
        mock_cursor.execute.assert_called_once_with('call sp_addUser(%s, %s, %s)', 
                                                     ('new_user', 'password', 'Full Name'))


if __name__ == '__main__':
    unittest.main()
