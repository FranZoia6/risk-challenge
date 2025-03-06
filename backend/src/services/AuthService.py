from src.database.db_mysql import get_connection
from src.utils.errors.CustomException import CustomException
from src.models.UserModel import User


class AuthService():

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
    
    @classmethod
    def add_user(cls, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call sp_addUser(%s, %s, %s)', (user.username, user.password, user.fullname))
                connection.commit()
            connection.close()
            return 'User added successfully'
        except CustomException as ex:
            raise CustomException(ex)




        