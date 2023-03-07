import string
extensions = ('.txt', '.docx')
file_name = input('Название файла: ').lower()
if file_name[0] in string.punctuation:
    print('Ошибка: название начинается на один из специальных символов')
elif not file_name.endswith(extensions):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')