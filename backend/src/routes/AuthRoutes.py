from flask import Blueprint, request, jsonify

import traceback


from src.utils.Logger import Logger
from src.models.UserModel import User
from src.utils.Security import Security
from src.services.AuthService import AuthService

main = Blueprint('auth_blueprint', __name__)

# Endpoint para iniciar sesión, genera un token si las credenciales son válidas.
@main.route('/login', methods=['POST'])
def login():
    try:
        username = request.json['username']
        password = request.json['password']

        _user = User(None, username, password, None)
        authenticated_user = AuthService.login_user(_user)

        if (authenticated_user != None):
            encoded_token = Security.generate_token(authenticated_user)
            return jsonify({'success': True, 'token': encoded_token})
        else:
            response = jsonify({'message': 'Unauthorized'})
            return response, 401
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        return jsonify({'message': "ERROR", 'success': False})

# Endpoint para registrar un nuevo usuario en el sistema.
@main.route('/signup', methods=['POST'])
def logUp():
    try:
        username = request.json['username']
        password = request.json['password']
        fullname = request.json['fullname']

        _user = User(None, username, password, fullname)
        response = AuthService.add_user(_user)

        if (response != None):
            return jsonify({'message': response, 'success': True,})
        else:
            response = jsonify({'message': response,'success': False, })
            return response, 401
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        return jsonify({'message': "ERROR", 'success': False})