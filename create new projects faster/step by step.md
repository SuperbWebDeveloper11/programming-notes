
### to start new django projects faster i use the following steps  


### Create virtual environment for you django project  
    virtualenv virtual_env_name -p /usr/bin/python3.8  
    cd virtual_env_name  
    source bin/activate 

### install dependencies 
    python -m pip install --upgrade pip 
    python -m pip install Django django-environ Pillow psycopg2-binary django-crispy-forms django-taggit sorl-thumbnail
    python -m pip install Django djangorestframework==3.11.1 django-environ drf_yasg Pillow psycopg2-binary django-crispy-forms 
 
### Create new django project 
    django-admin startproject project_name 
 
### Create PostgreSQL Role and Database: 
    sudo -i -u postgres  
    psql  
    CREATE ROLE role_name WITH SUPERUSER CREATEDB CREATEROLE LOGIN ENCRYPTED PASSWORD 'role_password' 
    CREATE DATABASE database_name; 
 
### Copy and Past some Folders and Files from an peaces of code 
    README.md 
    .gitignore 
 
    urls.py (comment out -accounts- app) 
    settings.py (modify ROOT_URLCONF, WSGI_APPLICATION and DATABASES) 
    .env (modify the file according to your postgrSQL role name and database name) 
 
    accounts/ 
    static/ 
    templates/ 
 
### Create superuser  
    python manage.py migrate 
    python manage.py createsuperuser 
 
### Create Profile manualy on the admin site 
     
 
### Start your creativity *&^%$@\$#%@#%&* 
 
