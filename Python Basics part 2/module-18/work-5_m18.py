while True:
    password = input('Придумайте пароль: ')
    title = len([sym for sym in password if sym.isupper()])
    nums = len([sym for sym in password if sym.isdigit()])
    if title >= 2 and nums >= 3 and len(password) >= 8:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')