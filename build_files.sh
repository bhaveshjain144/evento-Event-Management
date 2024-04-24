pip install -r requirements.txt
python3.12 manage.py collectstatic --noinput
# gunicorn app.wsgi:application -b 0.0.0.0:8000