from src.database.db_mysql import get_connection
from src.utils.errors.CustomException import CustomException
from src.models.UserModel import User


class AuthService():
      # Método para verificar las credenciales de un usuario durante el login.
    @classmethod
    def login_user(cls, user):
        try:
            connection = get_connection()
            authenticated_user = None
            with connection.cursor() as cursor:
                cursor.execute('call sp_verifyIdentity(%s, %s)', (user.username, user.password))
                row = cursor.fetchone()
                if row != None:
                    authenticated_user = User(int(row[0]), row[1], None, row[2])
            connection.close()
            return authenticated_user
        except CustomException as ex:
            raise CustomException(ex)
    
    # Método para agregar un nuevo usuario a la base de datos.
    @classmethod
    def add_user(cls, user):
        try:
            if not user.username or not user.password or not user.fullname:
                raise CustomException("All fields (username, password, fullname) are required.")


            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call sp_addUser(%s, %s, %s)', (user.username, user.password, user.fullname))
                connection.commit()
            connection.close()
            return 'User added successfully'
        
        except CustomException as ex:
            raise CustomException(ex)
        except Exception as ex:
            raise CustomException(f"An error occurred: {str(ex)}")




        