from src.database.db_mysql import get_connection
from src.models.UserModel import User
from src.utils.Logger import Logger
import traceback

class AuthService():
    # Método para verificar las credenciales de un usuario durante el login.
    @classmethod
    def login_user(cls, user):
        try:
            connection = get_connection()
            if not connection:
                Logger.add_to_log("error", "Database connection failed")
                return None

            authenticated_user = None
            with connection.cursor() as cursor:
                cursor.execute('call sp_verifyIdentity(%s, %s)', (user.username, user.password))
                row = cursor.fetchone()
                if row:
                    authenticated_user = User(int(row[0]), row[1], None, row[2])

            connection.close()
            return authenticated_user
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return None

    # Método para agregar un nuevo usuario a la base de datos.
    @classmethod
    def add_user(cls, user):
        try:
            if not user.username or not user.password or not user.fullname:
                Logger.add_to_log("error", "All fields (username, password, fullname) are required.")
                return False, "All fields are required."

            connection = get_connection()
            if not connection:
                Logger.add_to_log("error", "Database connection failed")
                return False, "Database connection failed"

            with connection.cursor() as cursor:
                cursor.execute('call sp_addUser(%s, %s, %s)', (user.username, user.password, user.fullname))
                connection.commit()

            connection.close()
            return True, "User added successfully"
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return False, "Error adding user"
