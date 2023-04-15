ip_address = input('Введите IP: ').split('.')
check = False
if len(ip_address) != 4:
    print('Адрес — это четыре числа, разделённые точками.')
else:
    for sym in ip_address:
        if sym.isdigit():
            check = True
            if int(sym) <= 255:
                check = True
            else:
                check = False
                print(f'{sym} превышает 255.')
                break
        else:
            check = False
            print(f'{sym} — это не целое число.')
            break
if check:
    print('IP-адрес корректен.')


