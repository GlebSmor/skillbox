depth = int(input('Введите глубину ямы: '))
count = 0
for row in range(1, depth + 1):
    for col in range(depth, 0, -1):
        print(col, end='')
    for col in range(1, depth + 1):
        if row == depth:
            print(col, end='')
    print()
