exp = int(input('Введите количество опыта: '))
level = 1
if (exp >= 1000) and (exp < 2500):
    level = level + 1
    print('Ваш уровень:', level)
elif (exp >= 2500) and (exp < 6000):
    level = level + 2
    print('Ваш уровень:', level)
elif exp >= 6000:
    level = level + 3
    print('Ваш уровень:', level)
    
