from src.database.db_mysql import get_connection
from src.utils.Logger import Logger
from src.models.RiskModel import Risk
import traceback

class RiskService():

    @classmethod
    def post_risk(cls, text):
        try:
            if not text.strip():
                return []

            connection = get_connection()
            if not connection:
                Logger.add_to_log("error", "Database connection failed")
                return []

            risks = []
            with connection.cursor() as cursor:
                cursor.callproc('sp_searchRisks', [text])
                resultset = cursor.fetchall()

                if resultset:
                    for row in resultset:
                        risk = Risk(int(row[0]), row[1], row[2], row[3], row[4], row[5])
                        risks.append(risk.to_json())

            connection.close()
            return risks
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return []

    @classmethod
    def get_risk(cls):
        try:
            connection = get_connection()
            if not connection:
                Logger.add_to_log("error", "Database connection failed")
                return []

            risks = []
            with connection.cursor() as cursor:
                cursor.callproc('sp_getRisk')
                resultset = cursor.fetchall()

                if resultset:
                    for row in resultset:
                        risk = Risk(int(row[0]), row[1], row[2], row[3], row[4], row[5])
                        risks.append(risk.to_json())

            connection.close()
            return risks
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return []

    @classmethod
    def update_risk(cls, risk_data):
        try:
            connection = get_connection()
            if not connection:
                Logger.add_to_log("error", "Database connection failed")
                return False, "Database connection failed"

            with connection.cursor() as cursor:
                cursor.callproc(
                    'sp_updateRisks',
                    [
                        risk_data["id"],
                        risk_data["cod"],
                        risk_data["impact"],
                        risk_data["title"],
                        risk_data["description"],
                        int(risk_data["resolved"])  
                    ]
                )
                connection.commit()  

            connection.close()
            return True, "Risk updated successfully"
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return False, str(ex)
