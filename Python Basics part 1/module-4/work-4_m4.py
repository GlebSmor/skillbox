stul_1 = int(input('Введите цену стула 1 '))
stul_2 = int(input('Введите цену стула 2 '))
stul_3 = int(input('Введите цену стула 3 '))
summa = stul_1 + stul_2 + stul_3
if summa > 10000:
    sale = summa - (summa / 10)
    print('Итог со скидкой:', sale)
else:
    print(('Скидок нет'))

