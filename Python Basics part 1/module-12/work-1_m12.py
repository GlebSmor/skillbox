def summa_n(number):
    count = 0
    for summ in range(1, number + 1):
        count += summ
    print('Я знаю, что сумма чисел от 1 до', number, 'равна', count)


number = int(input('Введите число: '))

summa_n(number)