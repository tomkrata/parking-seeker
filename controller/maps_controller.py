from flask_restx import Resource
from __main__ import app, maps_name_space
from service.maps_service import getLatLon


@maps_name_space.route("/latlon/<string:query>")
class LatLon(Resource):
    @app.doc(responses={200: 'OK'}, description="Get Latitude and Longtitude of a place")  # Documentation of route
    def get(self, query):
        _, coords = getLatLon(query)
        return coords
