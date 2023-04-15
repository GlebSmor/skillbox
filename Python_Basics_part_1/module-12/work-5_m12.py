def count_letters():
    text = input('Введите текст: ')
    number = input('Какую цифру ищем? ')
    letter = input('Какую букву ищем? ')
    count_letter = 0
    count_number = 0
    for symbol in text:
        if symbol == number:
            count_number += 1
        elif symbol == letter:
            count_letter += 1
    print('Количество цифр', number, ':', count_number)
    print('Количество букв', letter, ':', count_letter)


count_letters()
