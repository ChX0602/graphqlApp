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

In teledb/teledb/setting.py, change

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

On project level (same as crunchbase, teledb, manage.py), run
```
python manage.py runserver
```
Open browser and go to 
```
http://127.0.0.1:8000/graphiql?
```
If Firebox doesn't work, try Chrome.

## Sample queries
```
query {
  allObjects(first:20, name_Iexact:"Palantir Technologies") {
    totalCount
    edges {
      node {
        name
        domain
        homepageUrl
        overview
        foundedAt
        RNfundingRounds(raisedAmount_Gt:1000, fundedAt_Gt:"2000-01-01") {
          totalCount
          edges {
            node {
              fundingRoundType
              fundedAt
              raisedAmountUsd
              preMoneyValuation
              postMoneyValuation
              sourceDescription
              RNinvestments {
                totalCount
                edges {
                  node {
                    investorObject {
                      name
                      overview
                      investedCompanies
                      RNemployees {
                        totalCount
                        edges {
                          node {
                            title
                            startAt
                            relationshipObject {
                              name
                              overview
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```
