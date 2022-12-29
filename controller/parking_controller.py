from flask_restx import Resource
from __main__ import app, parking_name_space
from service.maps_service import getLatLon
from service.parking_service import getParkingZonesNearby
from flask import request, jsonify
import requests


@parking_name_space.route("/parking/<string:place>")
class NearbyParking(Resource):
    @app.doc(responses={200: 'OK'}, description="Get available parking nearby place")  # Documentation of route
    def get(self, place):
        limit = request.args.get('limit', default=100)
        range = request.args.get('range', default=1000)
        place, coords = getLatLon(place)
        response = requests.get("http://localhost:5000/utils/isholiday").json()
        parking_ids = getParkingZonesNearby(coords, holiday=response, limit=limit, range=range)
        return jsonify(parking_ids)
        # return "\n".join([f"{i + 1}: {str(x)}" for i, x in enumerate(parking_ids)])
