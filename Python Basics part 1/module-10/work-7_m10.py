quantity = int(input('Введите кол-во чисел: '))
count = 0
biggest = 0
biggest_number = 0
for numbers in range(quantity):
    number = int(input('Введите число '))
    backup = number
    while number != 0:
        remains = number % 10
        count += remains
        number = number // 10
    if biggest < count:
        biggest = count
        biggest_number = backup
    count = 0
print('Число', biggest_number, 'имеет максимальную сумму цифр:', biggest)

