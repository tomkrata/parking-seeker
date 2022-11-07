from flask import Flask, jsonify
from flask_restx import Api, Resource

if __name__ == "__main__":
    """Define Flask app"""
    flask_app = Flask(__name__)
    app = Api(app=flask_app,
              version="1.0",
              title="Parking seeker",
              description="Demo app for via")

    """Define namespace"""
    movies_name_space = app.namespace("movies", description='Get info about movies')
    """Run Flask app"""
    flask_app.run(debug=True)
