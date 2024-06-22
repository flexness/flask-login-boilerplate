import os

from flask import Flask, jsonify, request
from config import Config

from dotenv import load_dotenv
from dotenv import dotenv_values
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, current_user, SQLAlchemyUserDatastore, UserMixin, RoleMixin, auth_required
from flask_security.utils import hash_password
from .extensions import db, security
from .security import user_datastore


def create_app(config_class=Config):

    # create the Flask application instance
    app = Flask(__name__)

    # get values from config.py
    app.config.from_object(config_class)

    app.secret_key = app.config['SECRET_KEY']

    # initialize the SQLAlchemy database
    db.init_app(app)

   
    # Setup Flask-Security
    # user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    # Make `current_user` available in all templates
    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)
    
    # Import routes blueprint within the function to avoid circular imports
    from . import routes

    
    # Register blueprints directly with the Flask application instance
    app.register_blueprint(routes.routes_blueprint)


    # Create a user to test with if not existing
    # push context manually to app
    # with app.app_context():
        # create all tables if not existing
        # db.create_all()
        # create default test user if not existing
        # if not user_datastore.find_user(email="test@test.com"):
        #     user_datastore.create_user(email="test@test.com", password=hash_password("testtest"))
        # db.session.commit() 


    return app
