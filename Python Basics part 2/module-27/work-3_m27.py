import datetime
import functools


def logging(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        print(func.__name__, func.__doc__)
        try:
            func(*args, **kwargs)
        except Exception as error:
            logs = open('function_errors.log', 'w')
            logs.write(f'{func.__name__}\n{datetime.datetime.now()}\n{str(error)}')
            logs.close()
    return wrap


@logging
def test(a, b):
    '''
    Тестовая функция выводящая тестовый текст и сумму введенных чисел
    :param a: int
    :param b: int
    :return: sum of a and b
    '''
    # oshibka
    print('<Тут что-то происходит...>')
    print(a + b)


test(2, 4)