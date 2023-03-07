
def biggest(a, b, c):
    return max(max(a, b), max(b, c), max(a, c))


a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
print(biggest(a, b, c))


