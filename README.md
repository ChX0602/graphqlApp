# graphqlApp
Data Query API based on GraphQL


## Setup

1. In teledb/teledb/setting.py, change:

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

2. On project level (same as crunchbase, teledb, manage.py), run:
```
python manage.py runserver
```
Open browser and go to 
```
http://127.0.0.1:8000/graphiql?
```
