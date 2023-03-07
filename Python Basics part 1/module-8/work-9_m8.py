print('Задача 9. Выражение')
number_x = int(input('Введите число x: '))
denominator = 1
up = 1
down = 0
numerator = 1
result = 1
for number in range(1, 7):
    up = up * 2
    down = up - 1
    numerator = numerator * (number_x - down)
    denominator = denominator * (number_x - up)
    print(up, down, denominator, numerator)
if denominator == 0:
    print('Некорректное значение х, на 0 делить нельзя')
else:
    result = numerator / denominator
    print('res == ', result)

#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 