name = input('Введите имя должника: ')
dolg = int(input('Введите сумму долга: '))
print(name, 'ваша задолженность составляет', dolg, 'рублей.')
summa = 0
while summa < dolg:
    summa = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?'))
    if summa >= dolg:
        break
    print('Маловато,', name, '.', 'Давайте ещё раз.')
print('Отлично,', name, '! Вы погасили долг. Спасибо!')



