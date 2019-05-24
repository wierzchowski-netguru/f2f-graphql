## F2F project - GraphQL

#### Assumptions
* bare minimum regarding project setup, not even in docker

#### Stack
* Python 3.7
* SQLite as database
* Django 2.2 
* graphene 2.2.0
* jwt authentication

#### Project start
* clone repo and start terminal in project root
* `virtualenv -p python3.7 venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `./manage.py migrate`
* `./manage.py loaddata sampledb` (optional to populate db with some data)
* `./manage.py runserver`
* user to login is `seba:1234` (all users have password `1234`)

#### Project parts:
* v1 => simple GraphQL
* v2 => GraphQL + Relay

#### Collection with sample queries

* install Insomnia https://insomnia.rest/
* download collection from `collections/` dir and import it to Insomnia
* voila!
