from flask import Blueprint, request, jsonify
import traceback

# Logger
from src.utils.Logger import Logger
from src.utils.Security import Security
from src.services.RiskService import RiskService

main = Blueprint('risk_blueprint', __name__)


@main.route('/', methods=['GET'])
def get_risks():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            risk = RiskService.get_risk()
            if risk: 
                return jsonify({'risks': risk, 'message': "SUCCESS", 'success': True})
            else:
                return jsonify({'message': "No risks found", 'success': True})
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return jsonify({'message': "ERROR", 'success': False}), 500

@main.route('/', methods=['POST'])
def post_risks():
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            text = request.json.get('text', '')
            if not text:
                return jsonify({'message': "Missing 'text' field", 'success': False}), 400

            risk = RiskService.post_risk(text)
            if risk: 
                return jsonify({'risks': risk, 'message': "SUCCESS", 'success': True})
            else:
                return jsonify({'risks': [], 'message': "No matching risks", 'success': True})
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return jsonify({'message': "ERROR", 'success': False}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401
