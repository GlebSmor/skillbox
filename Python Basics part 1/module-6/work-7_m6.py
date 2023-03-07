import random
zagadka = random.randint(0, 10)
number = -1
counter = 0
while number != zagadka:
    number = int(input('Введите число: '))
    if number < zagadka:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    elif number > zagadka:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    counter += 1
print('Вы угадали!Число попыток:', counter)



