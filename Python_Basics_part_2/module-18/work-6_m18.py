string = input('Введите строку: ')
output = ''
for sym in string:
    if not len(output):
        output = sym + '1'
    else:
        if sym == output[-2]:
            output = '{}{}'.format(output[:-1], int(output[-1]) + 1)
        else:
            output = '{}{}{}'.format(output, sym, '1')

print(f'Закодированная строка:{output}')



