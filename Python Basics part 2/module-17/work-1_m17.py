string_list = []
output = []
string = input('Введите текст: ')
string_list.extend(string)
vowels = ['А', 'О', 'У', 'Ы', 'Э', 'Е', 'Ё', 'И', 'Ю', 'Я',
          'а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я']

for letter in string_list:
    if letter in vowels:
        output.extend(letter)

print('Список гласных букв:', output)
print('Длина списка:', len(output))
