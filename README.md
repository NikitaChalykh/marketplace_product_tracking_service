Тестовое задание REST API для отслеживания карточек товаров Wildberries
=====

Функциональные требования к проекту:
----------
Необходимо автоматическое отслеживание динамики изменения параметров карточки товара на 
маркетплейсе Wildberries, получение по запросу статистической 
информации о состоянии параметров карточки в заданном диапазоне дат с
заданным временным интервалом (не чаще 1 записи в час).

Описание проекта
----------
Проект разворачивается в следующих Docker контейнерах: web-приложение, postgresql-база данных, nginx-сервер, Redis-база данных и Celery-контейнер.

Реализована аутентификация на базе JWT-токенов, настроена админка. Информация об историческом состоянии карточек товаров фильтруется по 
диапазону дат с интервалом.

Задача коллекционирования данных реализована в виде асинхронных Celery задач.

Приготовлены фикстуры для звполнения БД тестовыми данными (пароль и никнейм админа в фикстурах БД - ```admin```).

Системные требования
----------
* Python 3.6+
* Docker
* Works on Linux, Windows, macOS, BS

Стек технологий
----------
* Python 3.8
* Django 3.1
* Django Rest Framework
* Pytest
* PostreSQL
* Nginx
* gunicorn
* Docker
* Selery
* Redis
* BeautifulSoup4

Установка проекта из репозитория (Linux и macOS)
----------
1. Клонировать репозиторий и перейти в него в командной строке:
```bash 
git clone 'https://github.com/NikitaChalykh/API_Parcer_TW.git'

cd API_Parcer_TW
```

2. Cоздать и открыть файл ```.env``` с переменными окружения:
```bash 
cd infra

touch .env
```

3. Заполнить ```.env``` файл с переменными окружения по примеру:
```bash 
echo DB_ENGINE=django.db.backends.postgresql >> .env

echo DB_NAME=postgres >> .env

echo POSTGRES_PASSWORD=postgres >> .env

echo POSTGRES_USER=postgres >> .env

echo DB_HOST=db >> .env

echo DB_PORT=5432 >> .env
```

4. Установка и запуск приложения в контейнерах:
```bash 
docker-compose up -d
```

5. Запуск миграций, создание суперюзера, сбор статики и загрузка фикстур:
```bash 
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py collectstatic --no-input 

docker-compose exec web python manage.py loaddata fixtures.json
```
Документация к проекту
----------
Документация для API после установки доступна по адресу ```/redoc/```, ```/swagger/```.
