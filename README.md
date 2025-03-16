Marketplace product tracking card service
=====

Project description
----------
The service is designed to automatically track changes in product card parameters on the marketplace. The service allows you to receive statistical data on the state of cards in a given date range, taking into account the update time interval (no more than 1 record per hour).

The project is deployed in the following Docker containers: web application, postgresql database, nginx server, Redis database and Celery container.

Authentication based on JWT tokens has been implemented, the admin panel has been configured, testing of the main models and URLs of the project has been implemented. Information about the historical state of product cards is filtered by a date range with intervals.

Tracking of card data is implemented as an asynchronous Celery task.

Fixtures have been prepared for filling the database with test data. Password and nickname of the admin in the DB fixtures - ```admin```.

System requirements
----------
* Python 3.8+
* Docker
* Works on Linux

Technology stack
----------
* Python 3.8+
* Django 3.1
* Django Rest Framework
* unittest
* PostreSQL
* Nginx
* gunicorn
* Docker, Docker Compose
* Сelery
* Redis
* BeautifulSoup4

Installing the project from the repository
----------
1. Cloning the repository:
```bash
git clone git@contest.idacloud.ru:Nikita223/marketplace_product_tracking_service.git

cd marketplace_product_tracking_service # Go to the directory with the project
```

2. Create a file ```.env``` using ```env.example``` as a template in the infra folder

3. Installing and running the application in containers:
```bash
docker compose up -d
```

4. Running migrations, collecting statics, loading fixtures and running tests:
```bash
docker compose exec web python manage.py migrate

docker compose exec web python manage.py collectstatic --no-input

docker compose exec web python manage.py loaddata fixtures.json

docker compose exec web python manage.py test
```

Working with the project
----------
Documentation on the API service:

```http://127.0.0.1/redoc/```

```http://127.0.0.1/swagger/```

Admin panel service:

```http://127.0.0.1/admin/```