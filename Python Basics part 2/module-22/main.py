import zipfile
import os

archive = 'voyna-i-mir.zip'
with zipfile.ZipFile(archive, 'r') as zip_file:
    zip_file.extractall()

syms_percent = {}
sorted_syms_percent = {}
count = 0

file = open('voyna-i-mir.txt', 'r', encoding='utf-8')
for line in file:
    line = line.strip(os.linesep)
    for sym in line:
        if sym.isalpha():
            count += 1
            if sym in syms_percent:
                syms_percent[sym] += 1
            else:
                syms_percent[sym] = 1
file.close()

for key, value in syms_percent.items():
    syms_percent[key] = value / count

sorted_keys = sorted(syms_percent, key=syms_percent.get, reverse=True)

for elem in sorted_keys:
    sorted_syms_percent[elem] = syms_percent[elem]
new_file = open('output.txt', 'w', encoding='utf-8')
new_file.write(f'-------------------\n'
               f'|Буква|  Частота  |\n')
for key, value in sorted_syms_percent.items():
    new_file.write(f'|  {key}  |{value:.8f} |\n')
new_file.write(f'-------------------\n')