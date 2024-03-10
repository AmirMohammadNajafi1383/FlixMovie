# Generate database migration files based on changes to Django models
python manage.py makemigrations --noinput

# Apply database migrations to the database
python manage.py migrate --noinput

# Collect all static files from Django apps into a single location
python manage.py collectstatic --noinput

# Run the Gunicorn server to serve the Django application
gunicorn --bind 0.0.0.0:8080 config.wsgi:application
