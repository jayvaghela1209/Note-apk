# Note-apk

A simple Flask note-taking web application with user signup/login, personal note creation, and note deletion.

## Features

- User registration and login
- Add text notes per user
- View only your own notes
- Delete notes you created
- PostgreSQL-backed data storage
- Deployable with Docker and Gunicorn

## Project Structure

- `run.py` — application entrypoint
- `app/__init__.py` — Flask app factory and database setup
- `app/models.py` — SQLAlchemy models for `User` and `Note`
- `app/routes/auth.py` — signup, login, logout routes
- `app/routes/notes.py` — note listing, creation, and deletion routes
- `app/templates/` — HTML templates
- `app/static/style.css` — basic styling
- `Dockerfile` — container build instructions
- `requirements.txt` — Python dependencies

## Requirements

- Python 3.12+ (or Docker)
- PostgreSQL database
- `pip` for dependency installation

## Environment Variables

The app reads database and secret settings from environment variables.

Required variables:

- `DB_HOST` — PostgreSQL host
- `DB_NAME` — database name 
- `DB_USER` — database user
- `DB_PASSWORD` — database password 
- `DB_PORT` — database port (default: `5432`)
- `SECRET_KEY` — Flask secret key

Optional:

- `FLASK_ENV=development` — run Flask in development mode

## Local Setup

1. Clone the repository.
2. Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set environment variables for your PostgreSQL database.

Example using a `.env` file:

```env
DB_HOST=localhost
DB_NAME=notes_db
DB_USER=postgre
DB_PASSWORD=your_password
DB_PORT=5432
SECRET_KEY=your_secret_key
FLASK_ENV=development
```

5. Create the PostgreSQL database and tables.

Use a PostgreSQL client or run SQL commands to create the database. Then create tables via Python shell:

```bash
python
>>> from app import create_app, db
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
```

6. Start the app:

```bash
python run.py
```

Then open `http://localhost:5000` in your browser.

## Docker Setup

Build and run the container:

```bash
docker build -t note-apk .
docker run -e DB_HOST=host.docker.internal -e DB_NAME=notes_db \
  -e DB_USER=postgre -e DB_PASSWORD=your_password \
  -e SECRET_KEY=your_secret_key -p 5000:5000 note-apk
```

If PostgreSQL is also containerized, connect via the appropriate Docker network host.

## Usage

- Visit `/signup` to create a new account.
- Log in at `/login`.
- Add notes on the notes page.
- Delete notes using the delete button next to each note.

## Notes

- Passwords are stored in plaintext in the database. For a production-ready app, replace this with hashed passwords using `werkzeug.security` or a similar library.
- The app currently uses server-side sessions and does not include email verification.
