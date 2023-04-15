def GCD(a,b):
    max = (a + b + abs(a - b)) // 2
    d = 0
    for i in range(1, max + 1):
        if a % i == 0 and b % i == 0:
            d = i
    print('НОД для', a, 'и', b, 'равен', d)


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
GCD(number_1, number_2)