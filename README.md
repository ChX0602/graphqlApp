# graphqlApp
Data Query API based on GraphQL

## Install dependencies. Django 1.9 is used in this exmaple

```
pip install graphene
pip install django
pip install graphene[django]
pip install django-graphiql
pip install django-filter
```
## Setup

1. In teledb/teledb/setting.py, change

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DBNAME',
        'USER': 'USERNAME',
        'PASSWORD': 'PASSWORD',
    }
}
```

2. On project level (same as crunchbase, teledb, manage.py), run
```
python manage.py runserver
```
3. Open browser and go to 
```
http://127.0.0.1:8000/graphiql?
```
If Firebox doesn't work, try Chrome.
