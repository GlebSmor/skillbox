def is_prime(number):
    if number < 2:
        return False
    for num in range(2, (number // 2) + 1):
        if number % num == 0:
            return False
    return True


def crypto(data):
    return [value for index, value in enumerate(data) if is_prime(index)]


# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(crypto('О Дивный Новый мир!'))