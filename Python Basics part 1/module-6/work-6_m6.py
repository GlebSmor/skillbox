vklad = int(input('Введите сумму вклада: '))
percent = int(input('Введите годовой процент: '))
itog = int(input('Введите окончательную сумму: '))
percent = percent / 100
years = 0
while vklad < itog:
    vklad = (vklad + vklad * percent) // 1
    years += 1
print ('Для достижения окончательной суммы понадобится', years)


