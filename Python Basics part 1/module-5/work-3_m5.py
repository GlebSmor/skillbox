mesto = int(input('Введите место в списке поступающих: '))
if mesto <= 10:
    balli = int(input('Введите количество баллов за экзамены: '))
    if balli >= 290:
       print('Поздравляем, вы поступили!')
       print('Бонусом вам будет начисляться стипендия.')
    elif mesto <= 10 and balli < 290:
         print('Поздравляем, вы поступили!')
         print('Но вам не хватило баллов для стипендии.')
elif mesto > 10:
    print('К сожалению, вы не поступили.')




