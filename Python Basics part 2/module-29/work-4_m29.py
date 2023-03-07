import functools


def singleton(cls):
    @functools.wraps(cls)
    def wrap(*args, **kwargs):
        if not wrap.instance:
            wrap.instance = cls(*args, **kwargs)
        return wrap.instance
    wrap.instance = None
    return wrap


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)