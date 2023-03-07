alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
            'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

capital_alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й',
                    'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
                    'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

coded_text = ''
text_list = []
text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
text_list.extend(text)
for sym in text_list:

    if sym in alphabet:
        for letter in range(0, len(alphabet) - 1):
            if sym == alphabet[letter]:
                if letter + shift > len(alphabet) - 1:
                    coded_text += alphabet[(letter + shift) - len(alphabet)]
                elif letter + shift <= len(alphabet) - 1:
                    coded_text += alphabet[letter + shift]

    elif sym in capital_alphabet:
        for letter in range(0, len(capital_alphabet) - 1):
            if sym == capital_alphabet[letter]:
                if letter + shift > len(capital_alphabet) - 1:
                    coded_text += capital_alphabet[(letter + shift) - len(capital_alphabet)]
                elif letter + shift <= len(capital_alphabet) - 1:
                    coded_text += capital_alphabet[letter + shift]

    elif sym not in alphabet and sym not in capital_alphabet:
        coded_text += sym

print('Зашифрованное сообщение:', coded_text)

