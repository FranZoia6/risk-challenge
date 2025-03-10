import os
import datetime
import jwt
import pytz
from dotenv import load_dotenv


class Security():
    load_dotenv()

    secret = os.getenv('JWT_KEY')
    tz = pytz.timezone("America/Buenos_Aires")
    
    
    # Genera un token JWT con los detalles del usuario autenticado.
    @classmethod
    def generate_token(cls, authenticated_user):
        payload = {
            'iat': datetime.datetime.now(tz=cls.tz),
            'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=100),
            'username': authenticated_user.username,
            'fullname': authenticated_user.fullname,
            'roles': ['Administrator', 'Editor']
        }
        return jwt.encode(payload, cls.secret, algorithm="HS256")

    # Verifica la validez de un token JWT recibido en los encabezados de la solicitud.
    @classmethod
    def verify_token(cls, headers):
        if 'Authorization' in headers.keys():
            authorization = headers['Authorization']
            encoded_token = authorization.split(" ")[1]

            if (len(encoded_token) > 0):
                try:
                    payload = jwt.decode(encoded_token, cls.secret, algorithms=["HS256"])
                    roles = list(payload['roles'])

                    if 'Administrator' in roles:
                        return True
                    return False
                except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                    return False

        return False