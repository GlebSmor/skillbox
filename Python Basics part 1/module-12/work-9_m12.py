import random


def rock_paper_scissors():
    user = input('\nВведите камень, ножницы или бумага: ')
    list = ['камень', 'ножницы', 'бумага']
    computer = random.choice(list)
    if user == 'камень' or user == 'ножницы' or user == 'бумага':
        print('\nПользователь:', user, '\nКомпьютер:', computer)
        if (computer == 'камень' and user == 'ножницы') or (computer == 'ножницы' and user == 'бумага') or (computer == 'бумага' and user == 'камень'):
            print('\nКомпьютер выиграл!')
        elif computer == user:
            print('\nНичья')
        else:
            print('\nПользователь выиграл!')
    else:
        print('\nОшибка ввода')
    choice = int(input('\nВведите:\n1 - чтобы сыграть еще раз \n2 - чтобы выйти в меню\n'))
    if choice == 1:
        rock_paper_scissors()
    elif choice == 2:
        mainMenu()


def guess_the_number():
    computer = random.randint(1, 10)
    print('Компьютер загадал число от 1 до 10\nПопробуй отгадать! ')
    while True:
        user = int(input('\nВведи число: '))
        if 1 <= user <= 10:
            if user == computer:
                print('Ты отгадал! Молодец!')
                break
            else:
                print('Не угадал! Попробуй еще раз')
        else:
            print('\nОшибка ввода')
            break
    choice = int(input('\nВведите:\n1 - чтобы сыграть еще раз \n2 - чтобы выйти в меню\n'))
    if choice == 1:
        guess_the_number()
    elif choice == 2:
        mainMenu()


def mainMenu():
    choice = int(input('Это главное меню\nВведите\n0 - чтобы выйти из приложения\n1 - чтобы сыграть в «Камень, ножницы, бумага»\n2 - чтобы сыграть в  «Угадай число»\n'))
    if choice == 1:
        rock_paper_scissors()
    elif choice == 2:
        guess_the_number()



mainMenu()