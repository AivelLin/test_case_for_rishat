# test_case_for_rishat
Тестовое задание для 'Ришат'

Текст задания находится в файле task.txt

## Как запустить проект:
Клонировать репозиторий на свой компьютер
```bash
git clone https://github.com/AivelLin/test_case_for_rishat
```

Перейти в папку test_case_for_rishat:
```bash
cd test_case_for_rishat/
```

Создать .env файл, с параметрами, как пример ниже:
``` 
    STRIPE_PUBLIC_KEY=pk_test_TYooMQauvdEDq54NiTphI7jx
    STRIPE_SECRET_KEY=sk_test_4eC39HqLyjWDarjtT1zdp7dc
    DB_ENGINE=django.db.backends.sqlite3
    DB_NAME=db.sqlite3
```

***
Подготовка перед запуском
-----------
***
Запустить docker-compose:

```bash
docker-compose up -d
```
Выполнить миграции:

```bash
docker-compose exec django python manage.py migrate
```

Собрать staticfiles:

```bash
docker-compose exec django python manage.py collectstatic --no-input
```

Создать пользователя с правами администратора:

```bash
docker-compose exec django python manage.py createsuperuser
```

Перейдите на страницу http://localhost:8000/admin/ для доступа админ панели

4242 4242 4242 4242 - тестовые данные номера карты для успешного платежа

4000 0025 0000 3155 - тестовые данные номера карты для ответа о необходимости аутентификации

4000 0000 0000 9995 - платеж будет отклонен

API 
http://localhost/item/<int:id>/ - выбор предмета для покупки
http://localhost/items/ - просмотреть все предметы
http://localhost/add_test_items/ - добавляет 4 тестовых предмета в базу данных

_Tech_stack:_
__Django, Stripe, Docker__
