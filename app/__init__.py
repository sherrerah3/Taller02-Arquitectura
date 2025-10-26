from flask import Flask
from .routes_api import api_bp
from .routes_view import view_bp
import os

def create_app():
    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
    app = Flask(__name__, template_folder=template_dir)
    app.register_blueprint(api_bp)
    app.register_blueprint(view_bp)
    return app
