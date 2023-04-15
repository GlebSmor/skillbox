import os


def gen_files_path(dir_path, dir_name):
    dir_path = os.walk(dir_path)
    for i_elem in dir_path:
        if dir_name in i_elem[0]:
            print(f'\nПуть до указаного каталога: {i_elem[0]}\n')
            break
        if i_elem[2]:
            for j_elem in i_elem[2]:
                yield os.path.join(i_elem[0], j_elem)


path = input('Введите путь до директории: ')
name = input('Введите название каталога: ')
print(*gen_files_path(path, name), sep='\n')