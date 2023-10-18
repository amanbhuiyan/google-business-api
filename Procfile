

release: python googleBusinessProject/manage.py makemigrations
release: python googleBusinessProject/manage.py migrate

web: gunicorn googleBusinessProject.googleBusinessProject.wsgi