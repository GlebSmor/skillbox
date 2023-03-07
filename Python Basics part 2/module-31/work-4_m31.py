import re
numbers = ['9999999999', '999999-999', '99999x9999']
count = 1
for num in numbers:
    if re.fullmatch(r'[89]\d{9}', num):
        print(f'{count}-й номер: всё в порядке')
    else:
        print(f'{count}-й номер: не подходит')
    count += 1