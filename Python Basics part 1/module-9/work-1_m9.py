day_week = input('Введите день недели: ')
count = 1
for day in ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'):
    if day == day_week:
        print(count)
    else:
        count += 1




