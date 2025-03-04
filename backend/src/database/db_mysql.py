import os
import pymysql
import traceback
from src.utils.Logger import Logger


def get_connection():
    try:
        return pymysql.connect(
            host=os.getenv('MYSQL_HOST', 'localhost'),
            user=os.getenv('MYSQL_USER', 'user'),
            password=os.getenv('MYSQL_PASSWORD', 'password'),
            db=os.getenv('MYSQL_DB', 'risk_db'),
            port=int(os.getenv('MYSQL_PORT', 3306))
        )
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
