import os


def stupid_calculator(string_in):
    string = string_in.split()
    if string[1] == '+':
        result = int(string[0]) + int(string[2])
    elif string[1] == '-':
        result = int(string[0]) - int(string[2])
    elif string[1] == '*':
        result = int(string[0]) * int(string[2])
    elif string[1] == '/':
        result = int(string[0]) / int(string[2])
    elif string[1] == '%':
        result = int(string[0]) % int(string[2])
    elif string[1] == '//':
        result = int(string[0]) // int(string[2])
    else:
        raise ValueError(f'Обнаружена ошибка в строке: {string_in}')
    return result


with open('calc.txt', 'r', encoding='utf-8') as file, open('errors.txt', 'w', encoding='utf-8') as error_file:
    summa = 0
    for line in file:
        line = line.strip(os.linesep)
        try:
            summa += stupid_calculator(line)
        except ValueError as error:
            error_file.write(str(error) + '\n')
            qst = input(f'{str(error)} Хотите исправить? ').lower()
            if qst == 'да':
                new_line = input('Введите исправленную строку: ')
                summa += stupid_calculator(new_line)
    print('Сумма результатов:', summa)
