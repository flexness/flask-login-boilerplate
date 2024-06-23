from app.factory import create_app, db
from app.models import Role
from flask_security.utils import hash_password
from app.security import user_datastore

def setup_app():
    app = create_app()  # Create the app instance

    with app.app_context():  # Push the app context
        db.create_all()  # Create all tables

        # Create roles if they do not exist
        if not Role.query.filter_by(name='admin').first():
            user_datastore.create_role(name='admin')
        if not Role.query.filter_by(name='user').first():
            user_datastore.create_role(name='user')

        # Create a default admin user if it does not exist
        if not user_datastore.find_user(email="admin@test.com"):
            admin_user = user_datastore.create_user(
                email="admin@test.com",
                password=hash_password("adminpassword")
            )
            user_datastore.add_role_to_user(admin_user, 'admin')

        # Create a default test user if it does not exist
        if not user_datastore.find_user(email="test@test.com"):
            test_user = user_datastore.create_user(
                email="test@test.com",
                password=hash_password("testtest")
            )
            user_datastore.add_role_to_user(test_user, 'user')

        db.session.commit()  # Commit the changes

    print("Setup complete!")

if __name__ == "__main__":
    setup_app()