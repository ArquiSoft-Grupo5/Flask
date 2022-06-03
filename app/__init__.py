from flask import Flask
from .config import Config
from .database import db

def create_app():
    """Método para la creación de la app de Flask."""
    app = Flask(name)
    app.config. from_object(Config)
    db.init_app(app)
    return app