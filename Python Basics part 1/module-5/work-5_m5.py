number_1 = int(input('Введите число 1: '))
number_2 = int(input('Введите число 2: '))
number_3 = int(input('Введите число 3: '))
if number_1 == number_2 == number_3:
    print('3 (3 числа равны)')
elif number_1 == number_2 or number_2 == number_3 or number_1 == number_3:
    print('2 (2 числа равны)')
else:
    print('0 (все числа разные)')





