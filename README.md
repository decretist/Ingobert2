# Ingobert2

Ingobert2 runs under Python 3.11.2 and Django 4.1.7 (15 March 2023).  
Ingobert2 runs under Python 3.7.2 and Django 2.1.5 (8 February 2019).  
Ingobert2 runs under Python 3.6.5 and Django 2.1.4 (27 December 2018).  
Ingobert2 runs under Python 3.6.5 and Django 2.0.4 (15 April 2018).  

If you have not worked with Ingobert2 recently, upgrade pip and Django:
```
sudo -H pip3 install --upgrade pip
sudo -H pip3 install --upgrade django
```
Installed packages are in
/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages

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
---
"In the beginning ..."
```
django-admin startproject mysite
mv -i mysite Ingobert2
cd Ingobert2
python3 manage.py startapp ingobert
python3 manage.py migrate
python3 manage.py runserver
```

[Writing your first Django app](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)  
[Python and Django tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-django)  
