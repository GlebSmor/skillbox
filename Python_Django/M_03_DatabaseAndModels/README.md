# Практическая работа 3  
# База данных и модели в Django

  

## Практика

### Практика. Видео 1

-   [ORM — Википедия](https://ru.wikipedia.org/wiki/ORM)
    
-   [SQLite](https://www.sqlite.org/index.html)
    

### Практика. Видео 2

-   [Models | Django documentation](https://docs.djangoproject.com/en/4.1/topics/db/models/)
    

### Практика. Видео 3

-   [Model field reference | Django documentation](https://docs.djangoproject.com/en/4.1/ref/models/fields/)
    

### Практика. Видео 4

-   [One-to-one relationships | Django documentation](https://docs.djangoproject.com/en/4.0/topics/db/examples/one_to_one/)
    
-   [Many-to-one relationships | Django documentation](https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/)
    
-   [Many-to-many relationships | Django documentation](https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_many/)
    

### Практика. Видео 5

-   [Model Meta options | Django documentation](https://docs.djangoproject.com/en/4.1/ref/models/options/)
    

  

## Цели практической работы 

-   Создать и запустить Django-приложение.
    
-   По очереди описать модели.
    
-   Сгенерировать и выполнить миграции для созданных моделей (по отдельности).
    
-   Создать связи между таблицами.
    
-   Создать веб-страницы на основе Django-шаблонов.
    
-   Вывести на страницу сущности из базы данных.
    

  
  

### Что нужно сделать

-   Проект mysite.
    
-   Приложение shopapp.
    
-   Приложение, установленное в настройках.
    
-   Модель Product с полями типов:
    

-   CharField;
    
-   TextField;
    
-   DecimalField;
    
-   PositiveSmallIntegerField;
    
-   DateTimeField;
    
-   BooleanField.
    

-   Модель Order с полями типов:
    

-   TextField;
    
-   CharField;
    
-   DateTimeField;
    
-   ForeignKey — связь с моделью User;
    
-   ManyToManyField — связь с моделью Product.
    

-   Выполнение стандартных миграций.
    
-   Отдельные миграции для каждой из моделей.
    
-   Пользователя через createsuperuser.
    
-   Management command в shopapp для создания продуктов через get_or_create (например, create_products.py).
    
-   Management command в shopapp для создания заказов через get_or_create (например, create_orders.py) и связи этих заказов с существующими продуктами.
    
-   View функции:
    

-   для shop index (список ссылок на доступные страницы);
    
-   для products list (список продуктов);
    
-   для orders list (список заказов с загруженными пользователями и продуктами).
    

-   Подключение view функций через urls.py внутри приложения.
    

  
  

### Советы и рекомендации

Если вы работаете через PyCharm, создание и активация виртуального окружения происходят автоматически.

  

### Что оценивается

-   Приложение установлено.
    
-   Модели описаны.
    
-   Миграции сгенерированы отдельно для каждой модели.
    
-   Связи между моделями настроены.
    
-   Django-шаблоны созданы.
    
-   Маршруты настроены.
    

  

### Как отправить работу на проверку

Сдайте практическую работу этого модуля через систему контроля версий Git сервиса Skillbox GitLab. В материалах с практической работой напишите «Сделано» и прикрепите ссылку на репозиторий.
