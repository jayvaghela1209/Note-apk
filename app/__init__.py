from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'

    db.init_app(app)
    from app.models import User, Note

    from app.routes import auth
    from app.routes import notes

    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(notes.notes_bp)

    
    with app.app_context():
        db.create_all()

    return app

