web: gunicorn glasmart.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
web: gunicorn --bind 0.0.0.0:$PORT hello:app
