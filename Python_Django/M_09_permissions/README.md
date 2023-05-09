# Практическая работа 9  
# Регистрация и права доступа

  

## Практика

### Видео 1. Регистрация

-   [https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.forms.UserCreationForm](https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.forms.UserCreationForm)
    

### Видео 2. Расширение модели пользователя

-   [https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#extending-the-existing-user-model](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#extending-the-existing-user-model)
    

### Видео 3. Групповые и персональные права

-   [https://docs.djangoproject.com/en/4.1/topics/auth/default/#groups](https://docs.djangoproject.com/en/4.1/topics/auth/default/#groups)
    
-   [https://docs.djangoproject.com/en/4.1/topics/auth/default/#permissions-and-authorization](https://docs.djangoproject.com/en/4.1/topics/auth/default/#permissions-and-authorization)
    
-   [https://docs.djangoproject.com/en/4.1/topics/auth/default/#programmatically-creating-permissions](https://docs.djangoproject.com/en/4.1/topics/auth/default/#programmatically-creating-permissions)
    

### Видео 4. Работа с правами в административной панели Django

-   [https://docs.djangoproject.com/en/4.1/topics/auth/default/#managing-users-in-the-admin](https://docs.djangoproject.com/en/4.1/topics/auth/default/#managing-users-in-the-admin)
    

### Видео 5. Использование и проверка прав

-   [https://docs.djangoproject.com/en/4.1/topics/auth/default/#permissions-and-authorization](https://docs.djangoproject.com/en/4.1/topics/auth/default/#permissions-and-authorization)
    
-   [https://docs.djangoproject.com/en/4.1/topics/auth/default/#default-permissions](https://docs.djangoproject.com/en/4.1/topics/auth/default/#default-permissions)
    
-   [https://docs.djangoproject.com/en/4.1/topics/auth/default/#permissions](https://docs.djangoproject.com/en/4.1/topics/auth/default/#permissions)
    

## Цель практической работы

Научиться настраивать параметры авторизации и устанавливать права доступа в Django.

  

## Что нужно сделать

Воспользуйтесь кодовой базой из пройденных модулей или файлами из репозитория [дополнительных материалов](https://gitlab.skillbox.ru/learning_materials/python_django_solutions/-/tree/master/module-materials/m09-perm).

  

1.  Поменяйте путь к myauth на accounts в корневом файле urls.py.
    
2.  В urls приложения myauth [подключите](https://docs.djangoproject.com/en/4.1/topics/auth/default/#module-django.contrib.auth.views) стандартные views, если ещё не настроены login и logout views. 
    
3.  Создайте модель Profile для расширения пользовательской модели.
    
4.  Добавьте возможность регистрации. При регистрации должен создаваться профиль пользователя.
    
5.  Создайте связь модели продукта с моделью пользователя, чтобы указать, кто создал продукт: добавьте колонку created_by. Продукт должен быть связан только с одним пользователем, но сам пользователь может создавать много продуктов.
    
6.  Дайте доступ к созданию продукта только тем, у кого есть разрешение (permission).
    
7.  При создании продукта по API свяжите его с пользователем, который выполняет запрос:
    

-   переопределите метод form_valid;
    
-   в form.instance.created_by укажите текущего пользователя;
    
-   используйте родительский метод (через super).
    

8.  [Воспользуйтесь переменной perms в шаблоне](https://docs.djangoproject.com/en/4.1/topics/auth/default/#permissions) и убедитесь, что ссылка на страницу создания продукта отображается только у пользователей с соответствующим доступом. При помощи объекта perms и тега if в шаблонах проверьте, доступно ли пользователю создание продуктов. Если доступно, то отобразите ссылку для перехода на страницу продукта. Если нет — не показывайте эту ссылку.
    
9.  Добавьте ограничение на редактирование продуктов:
    

-   суперпользователю вносить изменения в продукт можно всегда;
    
-   остальным — только если выполняются два условия: 
    

-   у пользователя есть разрешение на редактирование;
    
-   пользователь — автор продукта, который нужно отредактировать.
    

## Что оценивается

-   Приложение установлено и настроено.
    
-   Создана модель профиля пользователя.
    
-   Профиль пользователя создаётся при регистрации.
    
-   Установлено ограничение на создание продуктов.
    
-   Ссылка на создание продукта добавлена только на страницы пользователей, имеющих соответствующее разрешение.
    
-   Редактирование продукта доступно только:
    

-   суперпользователям,
    
-   создателям продукта, у которых есть право вносить изменения.
    

  

## Как отправить работу на проверку

Сдайте практическую работу через Skillbox GitLab. В поле сдачи практической работы напишите «Сделано» и прикрепите ссылку на репозиторий.

  