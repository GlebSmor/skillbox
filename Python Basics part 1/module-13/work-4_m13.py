text = str(input('Введите число в экспоненциальной форме: '))
number = ''
for symbol in text:
    if symbol != 'e':
        number += symbol
    if symbol == 'e':
        print('Манттиса:', number)
        number = ''
print('Порядок числа:', number)
