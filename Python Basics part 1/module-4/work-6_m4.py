number_1 = int(input('Кубик Кости: '))
number_2 = int(input('Кубик владельца: '))
if number_1 >= number_2:
    print('Разность:', number_1 - number_2)
    print('Игрок платит')
    print('Игра окончена')
else:
    print('Сумма:', number_1 + number_2)
    print('Владелец платит')
    print('Игра окончена')
    