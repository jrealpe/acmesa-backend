# ACMESA Django

This is acmesa Django setup using sqlite for local development.

## Start it

1. Download or clone this repository


	$ git clone https://github.com/jrealpe/acmesa-backend
2. Create virtulenv


	$ cd acmesa-backend
    $ python3 -m venv venv
3. Activate virtualenv


	$ source env/bin/activate
4. Install dependencies


    (env)$ pip install -r requirements
5. Create database


    (venv)$ python manage.py migrate
6. Create super user


    (venv)$ python manage.py createsuperuser
7. Run local server


    (venv)$ python manage.py runserver


## Web Admin
Open in your browser


	http://127.0.0.1:8000/admin
