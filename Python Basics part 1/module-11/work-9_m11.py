import math

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

D = b ** 2 - 4 * a * c

if D == 0:
    x1 = (-b - math.sqrt(D)) / (2*a)
    print('Корень равен', x1)
elif D > 0:
    x1 = (-b - math.sqrt(D)) / (2*a)
    x2 = (-b + math.sqrt(D)) / (2*a)

    if x1 > x2:
        print('Корни равны', x2, 'и', x1)
    else:
        print('Корни равны', x1, 'и', x2)
