count_neg = 0
count_pos = 0
number = 1
while number != 0:
    number = int(input('Введите число: '))
    if number > 0:
        count_pos += 1
    elif number < 0:
        count_neg += 1
print('Кол-во положительных чисел:', count_pos)
print('Кол-во отрицательных чисел:', count_neg)





