string = input('Введите троку из 10 символов a и b: ')
liters = 0
count = 0
for symbol in string:
    count += 2
    if symbol == 'b':
        liters += count
print('Всего', liters, 'литров за день')




