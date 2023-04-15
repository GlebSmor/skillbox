longest = ''
string = input('Введите строку: ').split()
for i in range(0, len(string)):
    if len(string[i]) > len(longest):
        longest = string[i]
print(f'Самое длинное слово: {longest}\nДлина этого слова: {len(longest)}')
