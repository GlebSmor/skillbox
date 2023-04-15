def zip_func(*args):
    min_len = min(map(len, args))
    iterators = [iter(iterable) for iterable in args]
    return (tuple(map(next, iterators)) for _ in range(min_len))


result = zip_func([1, 2, 3, 4], {'a': 4, 'b': 6, 'c': 7})
print(result, *result, sep='\n')

result = zip_func((1, 2, 3, 4), {'a': 4, 'b': 6, 'c': 7})
print(result, *result, sep='\n')

result = zip_func('func', {'a': 4, 'b': 6, 'c': 7})
print(result, *result, sep='\n')
