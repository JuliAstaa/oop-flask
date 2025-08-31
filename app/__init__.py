# import libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# load env
load_dotenv()

# inisialiasasi SQLAlchemy
db: SQLAlchemy = SQLAlchemy()

def create_app():
    app: Flask = Flask(__name__)

    abs_path = os.path.abspath(os.path.dirname(__file__))

    # konfigurasi aplikasi
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(abs_path, "contact.db")}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # koneksikan database sqlalchemy dengan flask
    db.init_app(app)

    # inilisiasliasi routing
    from . import routes
    app.register_blueprint(routes.main)

    return app
