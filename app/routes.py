
from flask import Blueprint, render_template, jsonify
from flask_security import roles_required, login_required
from .models import User


# set blueprint for routes 
routes_blueprint = Blueprint('routes', __name__)

# routes

@routes_blueprint.route("/")
@routes_blueprint.route("/index", methods=['GET', 'POST'])
def index():
 	return render_template('index.html')



@routes_blueprint.route('/users', methods=['GET'])
@roles_required('admin')
@login_required
def users():
    users = User.query.all()
    #users_list = [{'id': user.id, 'email': user.email, 'active': user.active} for user in users]
    #return jsonify(users_list)
    return render_template('users.html', users=users)