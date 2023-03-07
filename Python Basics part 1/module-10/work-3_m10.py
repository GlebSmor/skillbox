rows = int(input('Введите высоту рамки: '))
column = int(input('Введите ширину рамки: '))
for row in range(rows):
    for col in range(column + 2):
        if col == 0 or col == column + 1:
            print('|', end='')
        elif row == 0 or row == rows - 1:
            print('-', end='')
        else:
            print(' ', end='')
    print()
