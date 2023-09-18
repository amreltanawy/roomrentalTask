# Hotel Room Reservation

an interview task to develop a room reservation system with a specific requirements

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Database Schema

## Models ( database Tables)

### User Model
user model is a generic user profile data to support authentication and basic role assignment
#### Attributes
- pk 
- password
- is_email_verified
- name
- email
- is_active
- last_login
- is_superuser
- is_staff

### Room Model
Room model holds the most basic entity that can be reserved for a period of time given a price
#### Attributes
- pk
- name
- description 
- capacity
- price_per_night
- meta (a json field data type that allows for extra attributes to be added dynamically to support change of requirements)
- status ( active/inactive rooms)

### Reservation Model
Reservation model is the persistence of actual reservation requests that has been created on a room whether cancelled or not
#### Attributes
- pk
- user (a relationship with a single user due to many to one nature. each reservation is for 1 user)
- room (a relationship with a single room due to many to one nature. each reservation is for 1 room)
- status (active/inactive which resembles running/cancelled reservations)
- reservation_price (Total stay aggregation this where the final price  can be stored)
- check_in_date
- check_out_date
- meta (a json field data type that allows for extra attributes to be added dynamically to support change of requirements)

## Basic Commands

### Requirements

- Docker-compose installed follow [here](https://docs.docker.com/compose/install/) to install
- unix based operating system
- gitcli to clone the project

### Connecting to the docker container

- ensure you are at the home directory in your terminal

      $ docker-compose up

- after running the docker container run the following command to gain shell access to the container containing django

      $ docker exec -it hotel_room_reservation_local_django /bin/bash
### Setting Up Your Users


- To create a new user please use swagger endpoint at /api/docs/ where u will find a user/register endpoint

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

- To utilize the default user available

```
email = amr@test.com
password = test1234
```


For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.


### Swagger

Documentation for the endpoints are located at http://localhost:8000/api/docs/:


### Test coverage

To run the tests:
 make sure you are inside the docker container

    $ python manage.py test

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
