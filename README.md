# Tata-tz

[//]: # ([Zherdesh-web workflow])
## Стек технологий
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)



## Описание проекта
* Tata-tz - тестовое задание от TATA. 

## Документация к API
* Документация к API можно посмотреть тут: \

[//]: # ([https://app.mamod.io/api/v1/docs/swagger/]&#40;https://app.mamod.io/api/v1/docs/swagger/&#41;)
* В локальной версии:
[http://127.0.0.1:8000/api/v1/docs/swagger/](http://127.0.0.1:8000/api/v1/docs/swagger/)

[//]: # (## Локальный запуск&#40;Фронтендерам&#41;)

[//]: # (* Устанавливаем Docker)

[//]: # (* Устанавливаем Docker compose)

[//]: # (* Клонируем репозиторий)

[//]: # (* Создаем файл .env в корне проекта)

[//]: # (* Копируем в него настройки из файла .env.example)

[//]: # ()
[//]: # (Меняем настройки для подключения к БД в файле .env на:)

[//]: # ()
[//]: # (* PG_NAME = test)

[//]: # (* PG_USER = test)

[//]: # (* PG_PASS = 1234)

[//]: # (* PG_HOST = database)

[//]: # (* PG_PORT = 5432)

[//]: # ()
[//]: # (Для запуска прописываем:)

[//]: # ()
[//]: # (```bash)

[//]: # (docker compose -f docker-compose.frontend.yml up --build)

[//]: # (```)

## Локальный запуск

### Клонирование репозитория 

Обратите внимание на точку вконце, это говорит о том чтобы скопировать в текущую директорию

```bash
git clone https://github.com/Sino0on/zherdesh_web .
```

### Создание БД PostgreSQL

```bash
sudo -u postgres psql
```

```sql
CREATE USER name_user WITH PASSWORD 'password';
CREATE DATABASE name_db WITH OWNER name_user;
```

### Виртуальное окружение

```bash 
python3.10 -m venv venv &&
source venv/bin/activate &&
pip install -U pip &&
pip install -r requirements/dev.txt
```

> В Windows меняем строчку source venv/bin/activate на .\venv\Scripts\activate

> На продакшене меняем последнюю строчку на pip install -r requirements/prod.txt 

### Настройки окружения

1. Создаем файл .env в корне проекта
2. Копируем в него настройки из файла .env.example
3. Прописываем в нем свои значения

## Работа с репозиторием

### Установка новых зависимостей

При добавлении новых зависимостей нужно четко ответить себе на вопросы:
1. Является ли зависимость только для dev-а? 
2. Является ли зависимость только для prod-а?
3. Нужна ли она и там и там?

Допустим REQUIREMENT = название зависимости, которую мы хотим установить

```bash
pip install REQUIREMENT && pip freeze | grep REQUIREMENT >> requirements/dev.txt
```

Если в production, то в конце прописать prod.txt, вместо dev.txt

Если нужно и там и там, то:

```bash
pip install REQUIREMENT && 
pip freeze | grep REQUIREMENT >> requirements/dev.txt && 
pip freeze | grep REQUIREMENT >> requirements/prod.txt
```

### Настройки django

Файлы настроек:
* core/settings/base_settings - **Базовые** настройки
* core/settings/prod_settings - **Production** настройки
* core/settinng/dev_settings - **Development** настройки

Когда нам нужно добавить или изменить что-то в настройках мы должны сделать это в файле dev и в файле prod таким образом, чтобы обеспечить независимую работу как локально так и на проде
