def calculating_math_func(data, factorial={}):
    print(factorial)
    result = 1
    if data not in factorial:
        for index in range(1, data + 1):
            result *= index
        factorial[data] = result
    else:
        result = factorial[data]
    result /= data ** 3
    result = result ** 10
    return result


print(calculating_math_func(5))
print(calculating_math_func(6))
print(calculating_math_func(10))
print(calculating_math_func(5))
