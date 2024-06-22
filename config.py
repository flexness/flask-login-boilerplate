from dotenv import load_dotenv
import os
import secrets
    
# Load environment variables from .env file in development
load_dotenv()

# Generate a random password salt
# security_password_salt = secrets.token_hex(16)

class Config:
    
    # define baseurl based on env for using local validation service
    if os.getenv('FLASK_ENV') == 'development':
        print("this is dev") 
    elif os.getenv('FLASK_ENV') == 'production':
        print("this is prod")

    SECRET_KEY = os.getenv('SECRET_KEY')
    SECURITY_PASSWORD_SALT = 'security_password_salt'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:pw@ip:3306'
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'  # Set the password hash
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_REGISTER_URL = '/register'
    SECURITY_POST_REGISTER_VIEW = '/index'
