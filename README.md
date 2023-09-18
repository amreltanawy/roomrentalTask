# Hotel Room Reservation

an interview task to develop a room reservation system with a specific requirements

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

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
