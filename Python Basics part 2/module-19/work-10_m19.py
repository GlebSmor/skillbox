word = input('Введите строку: ').lower()
chars = set()

for i in word:
    if i in chars:
        chars.remove(i)
    else:
        chars.add(i)
print(('Можно', 'Нельзя')[len(chars) > 1], 'сделать полиндром')

