students = int(input('Введите колличество учеников: '))

troechniki = 0
otlichniki = 0
horoshisti = 0

for students_count in range(1, students + 1):
    number = int(input('Введите оценку ученика: '))
    if number == 3:
        troechniki += 1
    elif number == 4:
        horoshisti += 1
    elif number == 5:
        otlichniki += 1
if troechniki > horoshisti and troechniki > otlichniki:
    print('Сегодня больше троечников (', troechniki, ')')
elif horoshisti > troechniki and horoshisti > otlichniki:
    print('Сегодня больше хорошистов (', horoshisti, ')')
elif otlichniki > troechniki and otlichniki > horoshisti:
    print('Сегодня больше отличников (', otlichniki, ')')





