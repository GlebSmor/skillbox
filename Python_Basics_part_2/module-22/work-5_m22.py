import os


def edit_file(path, file):
    file = open(os.path.join(path, file), 'w+')
    file.write(text)
    file.seek(0)
    print(f'\nСодержимое файла:\n{file.read()}')
    file.close()


normal_path = ''
text = input('Введите строку: ')
path = input('\nКуда хотите сохранить документ? '
             'Введите последовательность папок (через пробел):\n').split()


for i_element in path:
    normal_path = os.path.join(normal_path, i_element)
normal_path = os.path.join(os.path.abspath('/'), normal_path)

if os.path.isdir(normal_path):
    file_name = input('\nВведите имя файла: ')
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    if os.path.isfile(os.path.join(normal_path, file_name)):
        qst = input('Вы действительно хотите перезаписать файл? ').lower()

        if qst == 'да':
            print('Файл успешно перезаписан!')
            edit_file(normal_path, file_name)

        else:
            print('Файл не изменен')

    else:
        print('Файл успешно сохранён!')
        edit_file(normal_path, file_name)

else:
    print('\nТакого католога не существует!')
    
