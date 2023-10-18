

release: python googleBusinessProject/manage.py makemigrations --no-input
release: python googleBusinessProject/manage.py migrate --no-input

web: gunicorn googleBusinessProject/googleBusinessProject.wsgi