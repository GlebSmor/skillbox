import os

files = 0
dirs = 0
size = 0

catalog = input('Введите путь до каталога: ')
tree = os.walk(catalog)

for i_element in tree:
    for j_element in i_element[2]:
        size += os.path.getsize(os.path.join(i_element[0], j_element))
    files += len(i_element[2])
    dirs += len(i_element[1])

print(f'\nКоличество файлов: {files}\n'
      f'Количество подкаталогов: {dirs}\n'
      f'Размер каталога (в Кб): {size / 1024:.2f}')
