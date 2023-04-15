contacts = {}
while True:
    action = int(input('\nВведите номер действия:\n1. Добавить контакт \n2. Найти человека\n'))

    if action == 1:
        name = input('Введите имя и фамилию нового контакта (через пробел): ').split()
        name = tuple(name)

        if name in contacts:
            print('Такой человек уже есть в контактах.')
            print(f'Текущий словарь контактов: {contacts}')

        else:
            phone = int(input('Введите номер телефона: '))
            contacts[name] = phone
            print(f'Текущий словарь контактов: {contacts}')

    elif action == 2:
        surname = input('Введите фамилию для поиска: ').capitalize()
        if surname.endswith('а'):
            surname = surname[:len(surname) - 1]
        check = False
        for key, value in contacts.items():
            if surname in key:
                print(key, value)
                check = True
        if not check:
            print('Такого человека нет в контактах')

    else:
        print('Ошибка ввода')
