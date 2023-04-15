string_1 = input('Первая строка: ')
string_2 = input('Вторая строка: ')
shift = ''
for num in range(len(string_2)):
    new_string = string_2[-num:] + string_2[:-num]
    if new_string == string_1:
        shift = num

if shift:
    print(f'Первая строка получается из второй со сдвигом {shift}.')
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

