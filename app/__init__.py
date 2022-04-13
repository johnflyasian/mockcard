from flask import Flask

from app.views.mock import mockresponse

flaskapp = Flask(__name__)

flaskapp.register_blueprint(mockresponse)

