from flask import request
from flask_restful import Resource
from src.utils.connection import conn
from datetime import datetime


class SunriseHandler(Resource):
    def get(self):
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM sunrise_schedule WHERE deleted is null or deleted = false')
            response = cur.fetchall()
        return {
            "sunrise_time": response[0][0].isoformat(),
            "sunrise_days": response[0][1],
            "current_time": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        }

    def post(self):
        payload = request.json
        with conn.cursor() as cur:
            cur.execute(
                "insert into sunrise_schedule(sunrise_time, sunrise_days) values(%s, %s)",
                (payload['sunrise_time'], payload['sunrise_days'])
            )