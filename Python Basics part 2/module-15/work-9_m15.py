word = input('Введите слово: ')
reversed_word = word[::-1]

if reversed_word == word:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
