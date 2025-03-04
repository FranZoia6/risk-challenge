from src.database.db_mysql import get_connection
from src.utils.Logger import Logger
from src.models.RiskModel import Risk
import traceback

class RiskService():

    @classmethod
    def post_risk(cls, text):
        try:
            connection = get_connection()
            if not connection:
                Logger.add_to_log("error", "Database connection failed")
                return []

            risks = []
            with connection.cursor() as cursor:
                words = text.split()
                conditions = " AND ".join(["(LOWER(impact) LIKE %s OR LOWER(title) LIKE %s OR LOWER(description) LIKE %s)"] * len(words))
                query = f"""
                    SELECT id, impact, title, description 
                    FROM risks 
                    WHERE {conditions}
                """
                
                params = [f"%{word.lower()}%" for word in words for _ in range(3)] 
                
                cursor.execute(query, params)
                resultset = cursor.fetchall()

                if resultset:
                    for row in resultset:
                        risk = Risk(int(row[0]), row[1], row[2], row[3])
                        risks.append(risk.to_json())

            connection.close()
            return risks
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return []
