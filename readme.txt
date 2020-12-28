Requirements:
1. Python 3.6 and above
2. Virtual Environment (pipenv or virtualenv)

Run the commands below after downloading and axtracting the DjangoWebApplication folder:
==================================================================================
$pip install virtualenv
$virtualenv newenv

$newenv/Scripts/activate (For Windows)
$newenv/bin/activate (For Linux)

(newenv)$cd DjangoWebApplication

(newenv)$pip install -r requirements.txt

(newenv)$python manage.py runserver
==================================================================================
Running Migrations:
Not required, as the web application will have sample data in the DB.

#python manage.py makemigrations
#python manage.py migrate
