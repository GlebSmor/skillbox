board_list = ['*' for _ in range(1, 10)]
win = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
       [0, 3, 6], [1, 4, 7], [2, 5, 8],
       [0, 4, 8], [2, 4, 6]]


def pick_cell(player):
    draw = False
    while True:
        if '*' not in board_list:
            print('Draw')
            draw = True
            break
        num = int(input(f'{player.name} pick a number (1-9): '))
        if board_list[num - 1] == '*':
            board_list[num - 1] = player.sym
            print(f'---------\n'
                  f'| {" ".join(board_list[:3])} |\n'  
                  f'| {" ".join(board_list[3:6])} |\n'
                  f'| {" ".join(board_list[6:9])} |\n'
                  f'---------')
            break
        else:
            print('Cell occupied')

    if draw:
        return True

    for i in win:
        if board_list[i[0]] == board_list[i[1]] == board_list[i[2]] == player.sym:
            print(f'{player.name} win')
            return True
    return False


class Player:
    def __init__(self, name, sym):
        self.sym = sym
        self.name = name


name = input('Player 1\nEnter name: ')
sym = int(input('Pick sym:\n1 - X\n2 - 0\n'))
name2 = input('Player2\nEnter name: ')
if sym == 1:
    player1 = Player(name, 'X')
    player2 = Player(name2, '0')
else:
    player1 = Player(name, '0')
    player2 = Player(name2, 'X')

print(f'{player1.name} == {player1.sym}')
print(f'{player2.name} == {player2.sym}')
print(f'---------\n'
      f'| {" ".join(board_list[:3])} |\n'  
      f'| {" ".join(board_list[3:6])} |\n'
      f'| {" ".join(board_list[6:9])} |\n'
      f'---------')


while True:
    if pick_cell(player1) or pick_cell(player2):
        break
