import string
text = input('Сообщение: ').split()
output = ''
for word in text:
    if word[len(word) - 1:] in string.punctuation:
        output += f'{(word[len(word) - 2::-1] + word[len(word) - 1:])} '
    else:
        output += f'{word[::-1]} '
print(f'Новое сообщение: {output}')

