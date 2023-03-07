string = input('Введите строку: ')
symbol_count = '0'
count = 1
for symbol in string:
    if symbol == symbol_count:
        if symbol == 's':
            count += 1
    else:
        count = 1
    symbol_count = symbol
print('Самая длинная последовательность: ', count)



