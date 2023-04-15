quantity = int(input('Введите кол-во чисел: '))
count = 0
for quantity_numbers in range(quantity):
    number = int(input('Введите число: '))
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    if prime:
        count += 1
        print(number)
print('Количество простых чисел в последовательности: ', count)
