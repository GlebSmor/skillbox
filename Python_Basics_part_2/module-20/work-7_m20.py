def tpl_sort(x_tuple):
    check = False
    for num in x_tuple:
        if isinstance(num, int):
            check = True
        else:
            check = False
            break
    if check:
        return tuple(sorted(x_tuple))
    else:
        return x_tuple


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
