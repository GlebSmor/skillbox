import functools


def counter(func):
    func.__count__ = 0

    @functools.wraps(func)
    def wrap(*args, **kwargs):
        func.__count__ += 1
        func(*args, **kwargs)
        print(f'Кол-во вызовов функции {func.__name__}: {func.__count__}')
    return wrap


@counter
def test(a, b):
    print('<Тут что-то происходит...>')
    print(a + b)


test(2, 3)
test(2, 7)
test(9, 3)