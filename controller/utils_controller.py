from datetime import datetime

from flask_restx import Resource
from __main__ import app, utils_name_space
from flask import request, jsonify

from service.utils_service import isHoliday


@utils_name_space.route("/isholiday")
class NearbyParking(Resource):
    @app.doc(responses={200: 'OK'}, description="Get available parking nearby place")  # Documentation of route
    def get(self):
        return isHoliday()
        # return "\n".join([f"{i + 1}: {str(x)}" for i, x in enumerate(parking_ids)])
