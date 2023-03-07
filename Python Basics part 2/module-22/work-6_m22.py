import string
count = 0

file = open('../Python_Basic/Module22/06_paranoia/text.txt', 'r')
new_file = open('cipher_text.txt', 'a')
for line in file:
    new_string = ''
    count += 1
    for sym in line:
        if sym in string.ascii_letters:
            num = ord(sym)
            new_string += chr(num + count)
    new_file.write(f'{new_string}\n')
file.close()
new_file.close()
