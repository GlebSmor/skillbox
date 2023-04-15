def towers(a, b, c):
    if a == 1:
        print(f'Переложить диск {1} со стержня номер {b} на стержень номер {c}')
    else:
        towers(a - 1, b, 6 - b - c)
        print(f'Переложить диск {a} со стержня номер {b} на стержень номер {c}')
        towers(a - 1, 6 - b - c, c)


qty = int(input('Введите количество дисков: '))
towers(qty, 1, 3)