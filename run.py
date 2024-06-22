from app.factory import create_app

# Create the Flask application instance
app = create_app()

# debug on/off
app.debug = True

# Run the Flask application
if __name__ == '__main__':
    app.logger.info("Starting the Flask application")
    app.run(port=5000, host='localhost')
