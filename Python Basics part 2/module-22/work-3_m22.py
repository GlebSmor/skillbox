import string
import os
zen = open('work-3/zen.txt', 'r')
lines_count = 0
words_count = 0
letters_count = 0
sym_list = {}
for line in zen:
    line = line.strip(os.linesep)
    words_list = line.split()
    lines_count += 1
    words_count += len(words_list)
    for sym in line:
        if sym in string.ascii_letters:
            letters_count += 1
            sym = sym.lower()
            if sym in sym_list:
                sym_list[sym] += 1
            else:
                sym_list[sym] = 1
zen.close()
output = [k for k, v in sym_list.items() if v == min(sym_list.values())]

print(f'Количество строк в файле: {lines_count}\n'
      f'Количество слов в файле: {words_count}\n'
      f'Количество букв в файле: {letters_count}\n'
      f'Наиболее редкая буква: {output[0]} она встречается '
      f'{min(sym_list.values())} раз(а)')
