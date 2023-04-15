word = input('Введите слово: ')
letters_list = list(word)
unique_list = []

for l_num in letters_list:                                                    # создаем список без повторов
    if l_num not in unique_list:
        unique_list.append(l_num)

for l_num in range(0, len(letters_list)):                                     # удаляем из нового списка повторы старого
    for l_num2 in range(l_num + 1, len(letters_list)):
        if (letters_list[l_num] == letters_list[l_num2]) and (letters_list[l_num2] in unique_list):
            unique_list.remove(letters_list[l_num2])

count = len(unique_list)
# print(letters_list) проверка списков
# print(unique_list)
print('Количество уникальных букв:', count)
