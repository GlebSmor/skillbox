phrase = input('Введите текст: ')
count = 0
for symbol in phrase:
    count += 1
    if symbol == '*':
        break
print('Символ ‘*’ стоит на позиции', count)





