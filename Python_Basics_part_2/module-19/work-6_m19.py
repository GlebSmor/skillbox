qty = int(input('Введите количество пар слов: '))
words_dict = {}
for num in range(1, qty + 1):
    pair = input(f'{num} пара: ').lower().split('-')
    words_dict[pair[0]] = pair[1]
    words_dict[pair[1]] = pair[0]
while True:
    word = input('Введите слово: ').lower()
    if words_dict.get(word) is not None:
        print('Синоним:', words_dict[word].title())
        break
    else:
        print('Такого слова в словаре нет.')
