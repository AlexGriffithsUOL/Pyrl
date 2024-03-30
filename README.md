### Set up
Download Python 3.11.8
Download the nvm packager manager
Install node 20.0.0
Run python -m venv .venv
Run .venv\Scripts\activate.bat
Run pip install -r requirements.txt
Run python manage.py migrate
In another terminal run python manage.py tailwind start
Run python manage.py collectstatic
Run python manage.py runserver

# Note: Leave the python manage.py runserver and tailwind start running in the background

It should now be accessible at http://127.0.0.1:8000/