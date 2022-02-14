# GIGA Assigment (Backend)
API for CRUD operation


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ejaj/assignment.git
$ cd assigment
```

Enable a virtual environment to install dependencies in and activate it:

```sh
$
$ source venv/bin/activate
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
(env)$ cd assigment
(env)$ python manage.py runserver
```

For creating Super user, you can run this command.
```sh
(env)$ python manage.py superuser
```

## Dependencies

```sh
- Database: PostgreSQL
```
Change the database name and password from .env file

API end point and response:
See the API documentation 
