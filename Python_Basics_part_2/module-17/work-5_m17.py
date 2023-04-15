string = input('Введите строку: ')
check = []
for sym in range(0, len(string)):
    if string[sym] == 'h':
        check.append(sym)
start = sorted(check)[0]
finish = sorted(check)[len(check) - 1]
output = string[start + 1:finish:]
print('Развёрнутая последовательность между первым и последним h:',
      output[::-1])
