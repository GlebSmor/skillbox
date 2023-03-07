print('Задача 6. Вклады')
contribution = int(input('Введите сумму вклада: '))
percent = int(input('Введите годовой процент: '))
result = int(input('Введите окончательную сумму: '))
percent = percent / 100
years = 0
while contribution < result:
    contribution = (contribution + contribution * percent) // 1
    years += 1
units = years % 10
tens = years // 10
if 1 < units < 5 and tens != 1:
  print ('Для достижения окончательной суммы понадобится', years, 'лет')
elif units == 1 and tens != 1:
  print ('Для достижения окончательной суммы понадобится', years, 'год')
elif units >= 5 or units == 0 or tens == 1:
  print ('Для достижения окончательной суммы понадобится', years, 'года')