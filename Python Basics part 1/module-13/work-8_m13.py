def factorial_num(n):
    factorial = 1
    for num in range(1, n + 1):
        factorial *= num
    return factorial


def degree_num(x, n):
    count = 1
    for num in range(1, n + 1):
        count = count * x
    return count


precision = float(input("Введите точность: "))
x = int(input("Введите икс: "))
ceil = 1
result = 0
n = 0

while abs(ceil) > precision:
    ceil = degree_num(-1, n) * (degree_num(x, (2 * n)) / factorial_num((2 * n)))
    result += ceil
    n += 1
print("Сумма ряда =", result)