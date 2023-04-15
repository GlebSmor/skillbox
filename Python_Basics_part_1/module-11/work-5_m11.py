import math

radius = float(input('Введите радиус случайной планеты: '))
volume = (4 / 3) * math.pi * radius ** 3
difference = float((10.8321 * 10**11) / volume)
if radius == 6371:
    print('Объём планеты Земля равен объему этой планеты')
else:
    if difference > 1:
        print('Объём планеты Земля больше в', round(difference, 3), 'раз')
    elif difference < 1:
        less = float(1 / difference)
        print('Объём планеты Земля меньше в ( 1 /', round(difference, 3), ') =', round(less, 3), 'раз')







