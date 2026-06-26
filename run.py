from app import db, create_app
from app.models import User, Note
import os

app = create_app()

if __name__ == "__main__":
    # Development
    if os.getenv('FLASK_ENV') == 'development':
        app.run(host="0.0.0.0", port=5000, debug=True)
    else:
        # Production - use gunicorn instead
        app.run(host="0.0.0.0", port=5000, debug=False)