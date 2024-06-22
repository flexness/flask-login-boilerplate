from dotenv import load_dotenv
import os
from datetime import timedelta
    
# Load environment variables from .env file in development
load_dotenv()

# Generated random salt with:
# import secrets
# security_password_salt = secrets.token_hex(16)


class Config:

 # Secret key for session management and CSRF protection
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Database connection string
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

    # Disable tracking modifications in SQLAlchemy (saves memory)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Salt for hashing passwords
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')

    # Enable user registration
    SECURITY_REGISTERABLE = True

    # Email confirmation required for registration (currently disabled)
    # SECURITY_CONFIRMABLE = True

    # Allow password recovery (resetting forgotten passwords)
    SECURITY_RECOVERABLE = True

    # Track user sign-ins (for security purposes)
    SECURITY_TRACKABLE = True

    # Hashing algorithm for passwords
    SECURITY_PASSWORD_HASH = 'bcrypt'

    # Disable sending an email on user registration
    SECURITY_SEND_REGISTER_EMAIL = False

    # URL for the registration page
    SECURITY_REGISTER_URL = '/register'

    # URL to redirect to after successful registration
    SECURITY_POST_REGISTER_VIEW = '/index'

    # Mail server settings for sending emails
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS') is not None
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL') is not None
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'your_default_sender@example.com')

    # Duration for which the session cookie is valid
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

    # Name of the session cookie
    SESSION_COOKIE_NAME = 'your_session_cookie_name'

    # HTTPOnly flag for the session cookie (enhances security)
    SESSION_COOKIE_HTTPONLY = True

    # Secure flag for the session cookie (set to True in production for HTTPS)
    SESSION_COOKIE_SECURE = False  # Set to True in production

    # Enable CSRF protection for forms
    WTF_CSRF_ENABLED = True

    # Secret key for CSRF protection
    WTF_CSRF_SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY')

    @staticmethod
    def print_config(app):
        print("Configuration Variables:")
        for key in app.config:
            print(f"{key}: {app.config[key]}")

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///boilerplate.db'
    SQLALCHEMY_ECHO = True

# Using an in-memory SQLite database (sqlite:///:memory:) is common for testing because it is fast
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}