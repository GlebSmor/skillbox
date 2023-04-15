import os

name = input('Введите свое имя: ')
while True:
    with open('chat_history.txt', 'a+', encoding='utf-8') as chat:
        try:
            qst = int(input('Выберите действие:\n'
                            '0 - Выйти\n'
                            '1 - Посмотреть текущий текст чата.\n'
                            '2 - Отправить сообщение.\n'
                            '3 - Стереть историю чата\n'
                            '4 - Сменить пользователя\n'))
            if qst == 0:
                print(f'Пользователь {name} вышел из чата')
                break
            elif qst == 1:
                chat.read()
                chat.seek(0)
                for line in chat:
                    line = line.strip(os.linesep)
                    print(line)
            elif qst == 2:
                message = input('Введите сообщение:\n')
                chat.write(f'{name}: {message}\n\n')
            elif qst == 3:
                chat.truncate(0)
            elif qst == 4:
                name = input('Введите свое имя: ')
            else:
                print('Ошибка ввода!\n')
        except ValueError:
            print('Ошибка ввода!\n')
