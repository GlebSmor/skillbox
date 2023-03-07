start = float(input('Введите начальную амплитуду: '))
finish = float(input('Введите амплитуду остановки: Введите амплитуду остановки: '))
count = 0
while start > finish:
    start *= 0.916
    count += 1
print('Маятник считается остановившимся через', count, 'колебаний')
