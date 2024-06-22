import base64

from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, jsonify

from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, auth_required, hash_password

from .models import db, User
from .security import user_datastore

from flask_security.utils import login_user, logout_user

# this 
routes_blueprint = Blueprint('routes', __name__)

# user_datastore = SQLAlchemyUserDatastore(db, User, Role)

###############################################
# routes
###############################################

@routes_blueprint.route("/")
@routes_blueprint.route("/index", methods=['GET', 'POST'])
def index():
 	return render_template('index.html')