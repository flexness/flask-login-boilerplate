import os

from flask import Flask
from flask_security import Security, current_user

from .extensions import db, security
from .security import user_datastore

# import config stuff
from config import Config, config

def create_app():

    # create the Flask application instance
    app = Flask(__name__)

    # get env var 
    env = os.getenv('FLASK_ENV', 'default')
    print("Environment set by .ENV: " + env)

    # get values from config.py
    app.config.from_object(config[env])

    app.secret_key = app.config['SECRET_KEY']

    # initialize the SQLAlchemy database
    db.init_app(app)

   
    # Setup Flask-Security
    security = Security(app, user_datastore)

    # in dev/debug print config vars
    show_config = False
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

    return app
