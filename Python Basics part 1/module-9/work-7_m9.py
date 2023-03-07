text = input('Введите текст: ')
count = 0
longest = 0
for symbol in text:
    if symbol != ' ':
        count += 1
    else:
        if count > longest:
            longest = count
        count = 0
print('Самое длинное слово, букв: ', longest)



