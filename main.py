from flask import Flask, jsonify
from flask_restx import Api, Resource

from service.maps_service import getLatLon

if __name__ == "__main__":
    """Define Flask app"""
    flask_app = Flask(__name__)
    app = Api(app=flask_app,
              version="1.0",
              title="Parking seeker",
              description="Demo app for via")
    """Define namespace"""
    maps_name_space = app.namespace("maps", description='Get info about maps')
    import controller.maps_controller
    """Run Flask app"""
    flask_app.run(debug=True)

