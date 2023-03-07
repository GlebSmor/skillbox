import math

quantity = int(input('Введите кол-во чисел: '))
for numbers in range(quantity):
    number = float(input('Введите число: '))
    if number > 0:
        if number % 1 != 0:
            number = int(number + 1)
        log = math.log(number)
        print('x =', number, 'log(x) =', log)
    elif number < 0:
        if abs(number) % 1 != 0:
            number = int(number - 1)
        exp = math.exp(number)
        print('x =', number, 'exp(x) =', exp)
        



