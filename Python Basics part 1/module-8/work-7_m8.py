print('Задача 7. Стипендия')
educational_grant = int(input('Введите стипендию:'))
expenses = int(input('Введите расходы на проживание: '))
total_expenses = 0
total_grant = 0
percent = 0
for months in range(0, 10):
    total_grant += educational_grant
    total_expenses = expenses + total_expenses + percent
    percent = total_expenses * (3 / 100)
print('У родителей необходимо попросить:', total_expenses - total_grant)
#Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# 
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.