from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Database Configuration from Environment Variables
    db_user = os.getenv('DB_USER', 'postgre')
    db_password = os.getenv('DB_PASSWORD', 'vaghela1209')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT', '5432')
    db_name = os.getenv('DB_NAME', 'notes_db')

    # RDS Connection String
    database_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    from app.models import User, Note

    from app.routes import auth
    from app.routes import notes

    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(notes.notes_bp)

    #with app.app_context():
    #    db.create_all()

    return app