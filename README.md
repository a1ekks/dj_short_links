### Django short links example (OLD python2.7)


**Project Installation Steps**

```
sudo apt-get install virtualenvwrapper python-all-dev postgresql-server-dev-all postgresql

git clone https://github.com/e1teck/dj_short_links.git

mkvirtualenv some_env

workon some_env

cd dj_short_links

pip install -r requirements.txt

define ur db settings in dj/settings.py

please give permission for database user to create some databases(need for testing out app)

python manage.py migrate

python manage.py createsuperuser (if you want use django-admin)

python manage.py runserver
```
