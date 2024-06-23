from .extensions import db
from flask_security import UserMixin, RoleMixin
import uuid

# define roles and users
roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), nullable=False)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())  
    last_login_at = db.Column(db.DateTime())     
    current_login_ip = db.Column(db.String(100)) 
    last_login_ip = db.Column(db.String(100))    
    login_count = db.Column(db.Integer())        
    fs_uniquifier = db.Column(db.String(64), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


