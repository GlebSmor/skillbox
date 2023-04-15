def zip_func(string, tuple_x):
    return ((string[i], tuple_x[i]) for i in range(min(len(string), len(tuple_x))))


result = zip_func('abcd', (10, 20, 30, 40))
print(result, *result, sep='\n')
