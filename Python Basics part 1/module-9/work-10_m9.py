word = input('Введите слово: ')
count = 0
first_half = ''
second_half = ''
for symbol in word:
    count += 1
    if count % 2 != 0:
        first_half += symbol
    elif count % 2 == 0:
        second_half += symbol
second_half = second_half[::-1]
print(first_half + second_half)






