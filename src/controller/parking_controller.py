from flask_restx import Resource
from __main__ import app, parking_name_space
from service.maps_service import getLatLon
from service.parking_service import getParkingZonesNearby
from flask import request, jsonify, session, flash, redirect, url_for
import requests


@parking_name_space.route("/parking")
class NearbyParking(Resource):
    @app.doc(responses={200: 'OK'}, description="Get available parking nearby place")  # Documentation of route
    def get(self):
        if session['username'] is None:
            flash('You are not signed in, the parking api will not work!')
            return redirect(url_for('par.park'))
        place = request.args.get('place', default='Prague')
        limit = request.args.get('limit', default=100)
        range = request.args.get('range', default=1000)
        place, coords = getLatLon(place)
        
        response = requests.get(request.url_root+"utils/isholiday").json()
        parking_ids = getParkingZonesNearby(coords, holiday=response, limit=limit, range=range)
        return jsonify(parking_ids)
        # return "\n".join([f"{i + 1}: {str(x)}" for i, x in enumerate(parking_ids)])
