number_factorial = int(input('Введите число: '))
result = 1
for number in range(1, number_factorial + 1):
    result *= number
print('Факториал числа', number_factorial, 'равен', result)



