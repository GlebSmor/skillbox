print('Задача 1. Космическая еда')
kg_total = 100
kg_month = - 4
months = 0
for kg in range(kg_total, 0, kg_month):
    months += 1
    print(months, '- й месяц', 'Осталось кг:', kg)
print('Гречки хватит на', months, 'месяцев')

#Ваш космический корабль потерпел крушение на пустынной планете.
# Еда здесь не растёт, но вы спасли из обломков 100-килограммовый мешок гречки.
# Из прошлого опыта вы знаете,
# что если будете экономно питаться, то у вас будет уходить по 4 килограмма гречки в месяц.
# 
# Чтобы прикинуть гречневый бюджет,
# вы решили написать программу, которая выведет информацию
# о том сколько килограммов гречки у вас должно быть в запасе через месяц, два и так далее,
# пока она не закончится.
# Используйте цикл for.