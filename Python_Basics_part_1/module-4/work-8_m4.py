number_1 = int(input('Введите число 1: '))
number_2 = int(input('Введите число 2: '))
number_3 = int(input('Введите число 3: '))

if number_1 > number_2 and number_1 > number_3:
    print(number_1, 'Больше')
elif number_2 > number_1 and number_2 > number_3:
    print(number_2, 'Больше')
elif number_3 > number_2 and number_3 > number_1:
    print(number_3, 'Больше')
    



