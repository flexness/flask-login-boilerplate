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


from config import config


def create_app():

    # create the Flask application instance
    app = Flask(__name__)

    # get values from config.py
    env = os.getenv('FLASK_ENV', 'default')
    app.config.from_object(config[env])

    app.secret_key = app.config['SECRET_KEY']

    # initialize the SQLAlchemy database
    db.init_app(app)

   
    # Setup Flask-Security
    # user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    # in dev/debug print config vars
    show_config = True
    with app.app_context():
        if app.config['DEBUG'] & show_config:  
            Config.print_config(app)


    # Make `current_user` available in all templates/jinja
    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)
    
    # Import routes blueprint within the function to avoid circular imports
    from . import routes

    
    # Register blueprints directly with the Flask application instance
    app.register_blueprint(routes.routes_blueprint)


    # Create a user to test with if not existing
    # push context manually to app
    with app.app_context():
        # create all tables if not existing
        db.create_all()
        # create default test user if not existing
        if not user_datastore.find_user(email="test@test.com"):
            user_datastore.create_user(email="test@test.com", password=hash_password("testtest"))
        db.session.commit() 


    return app
