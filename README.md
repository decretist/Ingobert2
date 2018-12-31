# Ingobert2

Ingobert2 runs under Python 3.6.5 and Django 2.1.4 (27 December 2018).
Ingobert2 runs under Python 3.6.5 and Django 2.0.4 (15 April 2018).

If you have not worked with Ingobert2 recently, upgrade pip and Django:
```
sudo -H pip3 install --upgrade pip
sudo -H pip3 install --upgrade django
```
Installed packages are in
/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages

After cloning Ingobert2 onto a new machine,
apply migrations, load data, and run server:
```
python3 manage.py migrate
python3 manage.py loaddata ingobert/fixtures/sample.xml
python3 manage.py runserver
```
If you make changes to the database:
```
python3 manage.py dumpdata ingobert.sample --indent 2 --format xml > sample.xml
python3 manage.py dumpdata ingobert.sample --indent 2 --format json > sample.json
python3 manage.py flush
```
(Paths need to be fixed.)

---
If you are setting up the development environment for the first time:
```
sudo -H pip3 install django
```
