from flask import Flask
from flask_restx import Api

if __name__ == "__main__":
    """Define Flask app"""
    flask_app = Flask(__name__)
    app = Api(app=flask_app,
              version="1.0",
              title="Parking seeker",
              description="Demo app for via")
    """Define namespace"""
    maps_name_space = app.namespace("maps", description='Get info about maps')
    parking_name_space = app.namespace("parking", description='Get info about parking spaces')
    utils_name_space = app.namespace("utils", description='Get various functions')
    import controller.maps_controller
    import controller.parking_controller
    import controller.utils_controller
    """Run Flask app"""
    flask_app.run(debug=True)

