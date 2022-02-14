# GIGA Assigment (Backend)
API for CRUD operation


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://kazi_ejaj@bitbucket.org/gpix/giga.git
$ cd assigment
```

Enable a virtual environment to install dependencies in and activate it:

```sh
$
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
For mac users
```sh
(env)$ pip install -r requirements.mac.txt
```
Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
To get initial data browse `http://127.0.0.1:8000/initial_news_api`

## Dependencies

```sh
- Database: PostgreSQL
```
Change the database name and password from .env file

API end point:
See the API documentation 
