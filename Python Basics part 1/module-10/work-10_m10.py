number = int(input('Введите глубину ямы: '))
print()
depth = number - 1
while depth >= 0:
    for pit in range(-number, number + 1):
        if abs(pit) > depth:
            print(abs(pit), end='')
        elif pit == 0:
            print(end='')
        else:
            print('.', end='')
    depth -= 1
    print()