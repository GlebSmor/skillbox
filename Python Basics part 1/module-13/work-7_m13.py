def calc_depth(start, end):
    return start + (end - start) / 2


def calc_danger(num):
    return num ** 3 - 3 * num ** 2 - 12 * num + 10


max_danger = float(input('Введите максимально допустимый уровень опасности: '))
depth_top = 0.0
depth_bottom = 4.0

if max_danger <= 0:
    print('Ошибка. Максимально допустимый уровень должен быть больше 0')
else:
    depth = calc_depth(depth_top, depth_bottom)
    danger = calc_danger(depth)
    while abs(danger) > max_danger:
        if danger > 0:
            depth_top = depth
        else:
            depth_bottom = depth
        depth = calc_depth(depth_top, depth_bottom)
        danger = calc_danger(depth)
    print('Приблизительная глубина безопасной кладки: ', depth, 'м')
