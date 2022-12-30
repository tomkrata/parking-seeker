from flask import Flask
from flask_restx import Api
from pymongo import MongoClient

if __name__ == "__main__":
    """Define Flask app"""
    flask_app = Flask(__name__, template_folder='templates')
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

    # blueprint for auth routes in our app
    from controller.user_controller import auth, master
    flask_app.register_blueprint(auth)
    flask_app.register_blueprint(master)

    # blueprint for non-auth parts of app
    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    """Run Flask app"""
    flask_app.run(debug=True)

