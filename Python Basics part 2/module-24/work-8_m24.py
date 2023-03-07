import random
suits = ['♣', '♦', '♥', '♠']
card_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
deck = {}
for i_suit in suits:
    deck[i_suit] = card_nums


def add_cards(qty=2):
    cards_list = []
    summa = 0
    for _ in range(qty):
        suit = random.choice(suits)
        sym = random.choice(deck[suit])
        deck[suit].remove(sym)

        if not isinstance(sym, int):
            if sym == 'A':
                num = 11
                if summa + num > 21:
                    num = 1
            else:
                num = 10
        else:
            num = sym
        summa += num
        card = f'-------\n' \
               f'|{sym}  {suit}|\n' \
               f'|     |\n' \
               f'|{suit}  {sym}|\n' \
               f'-------'
        cards_list.append(card)
    return summa, cards_list


class Player:
    def __init__(self, name, cards):
        self.name = name
        self.scores = cards[0]
        self.cards = cards[1]

    def info(self):
        print(f'Карты {self.name}:\n')
        print('\n'.join(self.cards))
        print('\nОчки = ', self.scores)


player = Player('Gleb', add_cards())
casino = Player('Casino', add_cards())
player.info()
while True:
    if player.scores >= 21:
        break
    qst = int(input('Хотите взять еще одну карту?\n'
                    '1 - Да\n'
                    '2 - Нет\n'))
    if qst == 1:
        new_card = add_cards(1)
        player.scores += new_card[0]
        player.cards.extend(new_card[1])
        player.info()
    else:
        break

if player.scores > 21 or player.scores < casino.scores:
    print(f'\n{player.name} проиграл(а)\n')
elif player.scores == casino.scores:
    print('\nНичья\n')
else:
    print(f'\n{player.name} выиграл(а)\n')

casino.info()
