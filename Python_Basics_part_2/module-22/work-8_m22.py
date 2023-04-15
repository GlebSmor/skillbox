import os
import string
syms_percent = {}
sorted_sym_percent = {}
count = 0

file = open('text.txt', 'r')
for line in file:
    line = line.strip(os.linesep)
    for sym in line.lower():
        if sym in string.ascii_letters:
            count += 1
            if sym in syms_percent:
                syms_percent[sym] += 1
            else:
                syms_percent[sym] = 1
file.close()

for key, value in syms_percent.items():
    value = round(value / count, 3)
    if value not in sorted_sym_percent:
        sorted_sym_percent[value] = list(key)
    else:
        sorted_sym_percent[value].append(key)

new_file = open('analysis.txt', 'w')
for key, value in sorted(sorted_sym_percent.items(), reverse=True):
    value = sorted(value)
    for letter in value:
        new_file.write(f'{letter}: {key}\n')
new_file.close()

