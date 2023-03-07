long = int(input('Введите общую длину колонтитула: '))
exclamation_point = int(input('Введите желаемое количество восклицательных знаков: '))
count = (long - exclamation_point) // 2
exclamation_point = '!' * exclamation_point
long = '~' * count
string = long + exclamation_point + long
print(string)



