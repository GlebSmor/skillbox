import os
count = 0
with open('people.txt', 'r', encoding='utf-8') as people_file, \
        open('errors.log', 'w', encoding='utf-8') as errors_file:
    for line in people_file:
        try:
            line = line.strip(os.linesep)
            count += len(line)
            if len(line) < 3:
                raise ValueError(f'Длина строки "{line}" меньше 3 символов')
        except ValueError as exc:
            errors_file.write(str(exc))
    print(f'Общая сумма символов: {count}')