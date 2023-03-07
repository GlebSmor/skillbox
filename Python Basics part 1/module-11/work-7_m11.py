print('Введите местоположение коня:')
x_horse = int((float(input('X: ')) * 10) // 1)
y_horse = int((float(input('Y: ')) * 10) // 1)
print('Введите местоположение точки на доске:')
x = int((float(input('X: ')) * 10) // 1)
y = int((float(input('Y: ')) * 10) // 1)
if (0 <= x_horse <= 7 and 0 <= y_horse <= 7) and (0 <= x <= 7 and 0 <= y <= 7):
    print('Конь в клетке (', x_horse, ',', y_horse, ').', 'Точка в клетке (', x, ',', y, ').')
    if ((x == x_horse + 2 or x == x_horse - 2) and (y == y_horse - 1 or  y == y_horse + 1)) or ((x == x_horse + 1 or x == x_horse - 1) and (y == y_horse - 2 or  y == y_horse + 2)):
        print('Да, конь может ходить в эту точку.')
    else:
        print('Нет, конь может ходить в эту точку.')
else:
    print('Были введены некорректные точки')




