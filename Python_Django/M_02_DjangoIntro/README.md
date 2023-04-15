# Практическая работа 2

# Введение в Django

## Практика

### Практика. Видео 1

- [Методы HTTP-запроса](https://developer.mozilla.org/ru/docs/Web/HTTP/Methods)

- [Заголовки HTTP](https://developer.mozilla.org/ru/docs/Web/HTTP/Headers)

- [Коды ответа HTTP](https://developer.mozilla.org/ru/docs/Web/HTTP/Status)

### Практика. Видео 2

- [Migrations | Django documentation](https://docs.djangoproject.com/en/4.0/topics/migrations/)

- [The Django admin site](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/)

- [django-admin and manage.py](https://docs.djangoproject.com/en/4.0/ref/django-admin/)

### Практика. Видео 3

- [URL dispatcher | Django documentation](https://docs.djangoproject.com/en/4.0/topics/http/urls/)

### Практика. Видео 4

- [Templates | Django documentation](https://docs.djangoproject.com/en/4.0/topics/templates/)

### Практика. Видео 5

- [Built-in template tags and filters丨Django documentation](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/)

## Цели практической работы

- Создать и запустить Django-приложение.

- Выполнить миграции.

- Создать суперпользователя.

- Создать и заполнить веб-страницу на основе Django-шаблона.

## Что нужно сделать

1. Создайте проект mysite.

2. Выполните стандартные миграции.

3. Создайте пользователя через createsuperuser.

4. Создайте приложение shopapp. Приложение должно быть установлено в настройках.

5. Создайте базовый шаблон.

6. Создайте шаблон на основе базового и view-функцию для отображения шаблона.  
   В шаблоне необходимо применить
   3 [тега](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#built-in-tag-reference) и
   3 [фильтра](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#built-in-filter-reference).  
   Передайте в шаблон контекст с объектами.

7. Подключите view-функцию в urls.py приложения.

## Советы и рекомендации

Если вы работаете через PyCharm, создание и активация виртуального окружения происходит автоматически.

## Что оценивается

- Приложение установлено.

- Базовый шаблон создан.

- Шаблон создан, в шаблон передан контекст, в шаблоне использовано 3 тега и 3 фильтра.

- Созданная view-функция возвращает отрисованный шаблон.

- Маршруты настроены.

## Как отправить работу на проверку

Сдайте практическую работу этого модуля через систему контроля версий Git сервиса Skillbox GitLab. В материалах с
практической работой напишите «Сделано» и прикрепите ссылку на репозиторий.
