import os


def check(string):
    errors = [IndexError('НЕ присутствуют все три поля'),
              NameError('Поле имени содержит НЕ только буквы'),
              SyntaxError('Поле «Имейл» НЕ содержит @ и .(точку)'),
              ValueError('Поле «Возраст» НЕ является числом от 10 до 99')]

    string = string.split()
    if len(string) != 3:
        raise errors[0]
    elif not string[0].isalpha():
        raise errors[1]
    elif ('@' and '.') not in string[1]:
        raise errors[2]
    elif not 10 <= int(string[2]) <= 99:
        raise errors[3]
    else:
        good_log.write(f'{line}\n\n')


with open('registrations.txt', 'r', encoding='utf-8') as file, open('registrations_good.log', 'w', encoding='utf-8') as good_log, \
        open('registrations_bad.log', 'w', encoding='utf-8') as bad_log:
    for line in file:
        line = line.strip(os.linesep)
        try:
            check(line)
        except (IndexError, NameError, SyntaxError, ValueError) as error:
            bad_log.write(f'{line}   {str(error)}\n\n')