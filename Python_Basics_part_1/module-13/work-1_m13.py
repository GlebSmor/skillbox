def number1(number):
    count = 0
    while number <= 1:
        number *= 10
        count += 1
    count = - count
    print('Формат плавающей точки: x =', round(number, 2), '* 10 **', count)


def number10(number):
    count = 0
    while number >= 10:
        number /= 10
        count += 1
    count = - count
    print('Формат плавающей точки: x =', round(number, 10), '* 10 **', count)


number = float(input('Введите число: '))
if 0 < number < 1:
    number1(number)
elif number > 1:
    number10(number)
else:
    print('Ошибка ввода')
