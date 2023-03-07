number_a = int(input('Введите число а: '))
number_b = int(input('Введите число b: '))
arithmetic_mean = 0
multiple_three = 0
for segment in range(number_a, number_b + 1):
    if segment % 3 == 0:
        arithmetic_mean += segment
        multiple_three += 1
arithmetic_mean = arithmetic_mean / multiple_three
print('Cреднее арифметическое всех чисел из отрезка [a; b], кратных числу 3 =', arithmetic_mean)





