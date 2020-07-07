# books
# Задание
Реализовать веб-сервис для библиотеки, управляющий тремя сущностями:
* 1 Книга - обязательные атрибуты: название, язык, год публикации;
* 2 Автор - обязательные атрибуты: фамилия, имя, отчество;
* 3 Подписчик - обязательные атрибуты: фамилия, имя, отчество, email.

Сервис должен предоставлять RESTful API для CRUD операций со всеми сущностями.
Дополнительно сервис должен предоставлять API метод search , который возвращает список
книг с запрошенным количеством авторов.

# Необязательная фича
При добавлении новой книги должна происходить email-рассылка всем подписчикам.

# Минимальные требования
* Python 3.7+
* Django 2.2+
* Django Rest Framework
* PostgreSQL 10+

# Definition of Done
Сервис должен запускаться командами:

```sh
git clone https://github.com/...
docker-compose up -d
```
Использование:
* Поиск: /api/v1/search?authors_count=1
* Docker/api.env - добавить email учетку:
```
# smpt mailing
EMAIL_SMTP_HOST=smtp.yandex.ru
EMAIL_SMTP_PORT=587
EMAIL_USERNAME=<your_login_here>
EMAIL_PASSWORD=<your_password_here>
```
