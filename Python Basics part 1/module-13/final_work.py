# MyProfile App Business Version

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone = ''
email = ''
index = ''
post_address = ''
additional_info = ''
# business information
OGRNIP = ''
INN = ''
payment_account = ''
bank_name = ''
BIK = ''
cor_account = ''


def general_info_user(name_par, age_par, phone_par, email_par, index_par, post_par, info_par):
    print(SEPARATOR)
    print('Имя:    ', name_par)
    if 11 <= age_par % 100 <= 19:
        years_parameter = 'лет'
    elif age_par % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_par % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_par, years_parameter)
    print('Телефон:', phone_par)
    print('E-mail: ', email_par)
    print('Индекс: ', index_par)
    print('Адрес:  ', post_par)
    if additional_info:
        print('\nДополнительная информация:')
        print(info_par)


def business_info_user(ogrnip_par, inn_par, payment_account_par, bank_name_par, bik_par, cor_account_par):
    print('\nИнформация о предпринимателе')
    print('ОГРНИП: ', ogrnip_par)
    print('ИНН:    ', inn_par)
    print('Банковские реквизиты')
    print('Р/с:    ', payment_account_par)
    print('Банк:   ', bank_name_par)
    print('БИК:    ', bik_par)
    print('К/с:    ', cor_account_par)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while 1:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name_update = input('Введите имя: ')
                if name_update != '':
                    name = name_update
                while 1:
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')

                update_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                if update_phone != '':
                    phone = ''
                    for ch in update_phone:
                        if ch == '+' or ('0' <= ch <= '9'):
                            phone += ch

                email_update = input('Введите адрес электронной почты: ')
                if email_update != '':
                    email = email_update
                update_index = input('Введите почтовый индекс: ')
                if update_index != '':
                    index = ''
                    for ch in update_index:
                        if '0' <= ch <= '9':
                            index += ch

                post_address_update = input('Введите почтовый адрес (без индекса): ')
                if post_address_update != '':
                    post_address = post_address_update
                additional_info_update = input('Введите дополнительную информацию:\n')
                if additional_info_update != '':
                    additional_info = additional_info_update

            elif option2 == 2:
                # input business information
                while 1:
                    OGRNIP_update = int(input('Введите ОГРНИП: '))
                    OGRNIP = OGRNIP_update
                    count = 0
                    while OGRNIP_update > 0:
                        OGRNIP_update //= 10
                        count += 1
                    if count != 15:
                        print('ОГРНИП должен содержать 15 цифр')
                    elif count == 15:
                        break
                INN = int(input('Введите ИНН: '))
                while 1:
                    payment_account_update = int(input('Введите расчётный счёт: '))
                    payment_account = payment_account_update
                    count = 0
                    while payment_account_update > 0:
                        payment_account_update //= 10
                        count += 1
                    if count != 20:
                        print('Расчётный счёт должен содержать 20 цифр')
                    elif count == 20:
                        break
                    payment_account = payment_account_update
                bank_name_update = input('Введите название банка: ')
                if bank_name_update != '':
                    bank_name = bank_name_update
                BIK = int(input('Введите БИК: '))
                cor_account = int(input('Введите корреспондентский счёт: '))
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone, email, index, post_address, additional_info)

            elif option2 == 2:
                general_info_user(name, age, phone, email, index, post_address, additional_info)

                # print business information

                business_info_user(OGRNIP, INN, payment_account, bank_name, BIK, cor_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
