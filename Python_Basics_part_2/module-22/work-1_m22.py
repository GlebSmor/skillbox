import string
file = open('work-1/numbers.txt', 'r')
file.seek(0)
summa = 0
for sym in file.read():
    if sym in string.digits:
        summa += int(sym)
file.close()
output = open('answer.txt', 'w')
output.write(str(summa))
output.close()
