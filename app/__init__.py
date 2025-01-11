from flask import Flask
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.secret_key = "supersecretkey"

    from .routes import main
    app.register_blueprint(main)

    return app
