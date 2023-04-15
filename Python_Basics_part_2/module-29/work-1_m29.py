import functools
from typing import Callable


def check_permission(user: str):
    def permission(func: Callable):
        @functools.wraps(func)
        def wrap():
            if user in user_permissions:
                func()
            else:
                raise PermissionError(f'У пользователя {user} недостаточно прав, чтобы выполнить функцию {func.__name__}')
        return wrap
    return permission


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


try:
    delete_site()
    add_comment()
except PermissionError as er:
    print(str(er))