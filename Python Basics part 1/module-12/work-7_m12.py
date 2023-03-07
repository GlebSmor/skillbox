def minimum_number():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    minimum = (a + b - abs(a - b)) // 2
    print('Минимальное число: ', minimum)


minimum_number()