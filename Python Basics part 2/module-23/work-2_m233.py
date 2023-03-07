import random
import os


def plus_function(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def minus_function(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


with open('coordinates.txt', 'r') as file, open('result.txt', 'w') as result_file:
    for line in file:
        line = line.strip(os.linesep)
        nums_list = line.split()
        try:
            res1 = plus_function(int(nums_list[0]), int(nums_list[1]))
            res2 = minus_function(int(nums_list[0]), int(nums_list[1]))
        except ValueError:
            print('Некорректный данные в файле "coordinates.txt"')
            break
        except ZeroDivisionError:
            print('Произошло деление на ноль')
            break
        number = random.randint(0, 100)
        my_list = sorted([res1, res2, number])
        my_list = [str(sym) for sym in my_list]
        result_file.write(f'{", ".join(my_list)}\n')