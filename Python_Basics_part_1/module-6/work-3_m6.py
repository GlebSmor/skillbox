number = int(input('Введите число: '))
x = number
count = 0
while number > 0:
    number = number // 10
    count += 1
print('В числе', x, count, 'цифр')


