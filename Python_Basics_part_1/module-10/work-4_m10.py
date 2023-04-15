size = int(input('Введите размер: '))

for row in range(size):
    for col in range(size):
        if col == row or col == -row + size - 1:
            print('^', end='')
        else:
            print(' ', end='')
    print()
    