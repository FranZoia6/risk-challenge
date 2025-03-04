from flask import Flask
from flask_cors import CORS
from .routes import RiskRoutes, AuthRoutes

def init_app(config):
    app = Flask(__name__)  
    CORS(app, resources={r"/*": {"origins": "*"}}) 

    app.config.from_object(config)  
    app.register_blueprint(RiskRoutes.main, url_prefix='/risk')
    app.register_blueprint(AuthRoutes.main, url_prefix='/auth')

    return app
