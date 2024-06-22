from app.factory import create_app

app = create_app()

# Run the Flask application
if __name__ == '__main__':
    app.logger.info("Starting the Flask application")
    app.run(port=5000, host='localhost')
