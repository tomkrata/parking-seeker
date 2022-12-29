from flask import Flask, jsonify
from flask_restx import Api, Resource
import json
from __main__ import app, maps_name_space
from service.maps_service import getLatLon

print("I WAS HERE")


@maps_name_space.route("/latlon/<string:query>")
class LatLon(Resource):
    @app.doc(responses={200: 'OK'}, description="Get Latitude and Longtitude of a place")  # Documentation of route
    def get(self, query):
        _, coords = getLatLon(query)
        return coords
