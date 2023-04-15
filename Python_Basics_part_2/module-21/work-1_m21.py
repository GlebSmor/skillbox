def challenge(num, x=1):
    if num < x:
        return 0
    print(x)
    challenge(num, x + 1)


number = int(input('Введите num: '))
challenge(number)
