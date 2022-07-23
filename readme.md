# fashion-web-app

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development.

---

## Prerequisites

You need the following modules and dependencies installed to run this project:

- Install Python 3.8
- Install [docker](https://www.docker.com/products/docker-desktop).
- Install [docker-compose](https://docs.docker.com/compose/).

---

## Installing locally on your system and running the app

Simply, run the following command to install the project dependencies and running it:

```
$ docker-compose up -d --build
```

---

The application will run on http://127.0.0.1:8000/.

---

## Apply the migrtions

Simply, run the following command to apply the migrations

```
$ docker-compose exec web python manage.py migrate
```

---

## **Built With**

- [**Python**](https://www.python.org/)
- - [DRF](https://www.django-rest-framework.org/)
- - [Django](https://www.djangoproject.com/)
