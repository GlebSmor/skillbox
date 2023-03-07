number = int(input('Введите число: '))
counter = 1
sum_factorial = 0
for factorial in range(1, number + 1):
    counter *= factorial
    sum_factorial += counter
print('Сумма факториалов числа', number, 'равна', sum_factorial)

