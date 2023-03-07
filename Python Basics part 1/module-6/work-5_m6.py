hours = 1
done_tasks = 0
call = 0
print('Начался восьмичасовой рабочий день.')
while hours <= 8:
    print(hours, '- й час')
    tasks = int(input('Сколько задач решит Максим? '))
    done_tasks = done_tasks + tasks
    call = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    hours += 1
print('Рабочий день закончился. Всего выполнено задач:', done_tasks)
if call == 1:
    print('Нужно зайти в магазин.')
    