import random
import os
result = 0
check = False
with open('result.txt', 'w+') as result_file:
    while result < 777:
        try:
            number = int(input('Введите число: '))
            result += number
            if 13 == random.randint(1, 13):
                raise Exception
            result_file.write(str(number) + '\n')
        except ValueError:
            print('Введено не число')
        except Exception:
            check = True
            print('Вас постигла неудача!')
            break
    if not check:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
    result_file.read()
    result_file.seek(0)
    print(f'Содержимое файла:')
    for line in result_file:
        line = line.strip(os.linesep)
        print(line)
