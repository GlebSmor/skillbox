text = input("Введите текст: ")

frequency = {}
for sym in sorted(text):
    if sym in frequency:
        frequency[sym] += 1
    else:
        frequency[sym] = 1


print('\nИнвертированный словарь частот:')
for letter, freq in frequency.items():
    print(letter, ':', freq)


print('\nИнвертированный словарь частот:')
invert = {}
for letter, num in frequency.items():
    invert.setdefault(num, []).append(letter)
for sym in sorted(invert):
    print(sym, ':', invert[sym])
