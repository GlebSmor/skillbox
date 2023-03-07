import functools
from typing import Callable, Any


def how_are_you(func: Callable):
    @functools.wraps(func)
    def wrap(*args, **kwargs) -> Any:
        inp = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        func(*args, **kwargs)
    return wrap


@how_are_you
def test(a: int, b: int) -> None:
    print('<Тут что-то происходит...>')
    print(a + b)


test(10, 45)