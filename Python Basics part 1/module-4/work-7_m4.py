hours = int(input('Введите отработанные часы: '))
credit = int(input('Введите остаток по кредиту: '))
food = int(input('Введите траты на еду: '))
zarplata = ((200 * hours) / (2**3)) + hours
summa = credit + food
if zarplata >= summa:
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать больше!')


