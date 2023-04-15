from datetime import datetime
import time


def timer(cls, func, date_format):
    def wrap(*args, **kwargs):
        out_format = date_format
        for sym in out_format:
            if sym.isalpha():
                out_format = out_format.replace(sym, '%' + sym)

        print(f'Запускается "{cls.__name__}.{func.__name__}". '
              f'Дата и время запуска: {datetime.now().strftime(out_format)}')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Завершение "{cls.__name__}.{func.__name__}", '
              f'время работы = {round(end - start, 3)} сек.')
        return result
    return wrap


def log_methods(date_format):
    def decorate(cls):
        for method in dir(cls):
            if not method.startswith('_'):
                cur_method = getattr(cls, method)
                decorated_method = timer(cls, cur_method, date_format)
                setattr(cls, method, decorated_method)
        return cls
    return decorate


@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()