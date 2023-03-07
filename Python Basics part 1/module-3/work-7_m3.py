number = int(input('Введите число: '))
thousnds = (number // 1000)
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
ones = (number % 10)
print(thousnds, hundreds, tens, ones )
