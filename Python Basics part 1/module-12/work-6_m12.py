def check_coordinate(x, y):
    if abs(x) > area or abs(y) > area:
        print('Монетки в области нет.')
    else:
        print('Монетка где-то рядом.')


area = 1

coordinate_x = int(input('Введите координату X: '))
coordinate_y = int(input('Введите координату Y: '))

check_coordinate(coordinate_x, coordinate_y)
