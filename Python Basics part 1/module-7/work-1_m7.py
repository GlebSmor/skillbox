count = 0
for number in range(10):
    number = int(input('Введите число: '))
    if number % 2 == 0 and number > 0:
        count += 1
print('Число четных и положительны номеров = ', count)



