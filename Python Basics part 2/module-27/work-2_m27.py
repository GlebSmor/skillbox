import functools
import time


def speed_downgrade(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        time.sleep(5)
        func(*args, **kwargs)
    return wrap


@speed_downgrade
def test(a, b):
    print('<Тут что-то происходит...>')
    print(a + b)


test(2, 5)