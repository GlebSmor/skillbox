guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    if len(guests) == 0:
        print('\nВечеринка закончилась, все разошлись по домам')
        break

    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    question = input('Гость пришёл или ушёл? ')

    if question == 'Пора спать':
        print('\nВечеринка закончилась, все легли спать.')
        break

    name = input('Имя гостя: ')
    if question == 'пришёл':
        if len(guests) < 6:
            guests.append(name)
            print('Привет', name, '!')
        else:
            print('Прости,', name, ', но мест нет.')

    elif question == 'ушёл':
        guests.remove(name)
        print('Пока,', name, '!')
