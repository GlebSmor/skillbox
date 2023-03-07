cards = int(input('Введите количество карточек: '))
lost_card = 0
for cards_count in range(1, cards + 1):
    lost_card += cards_count
for cards_count in range(1, cards):
    card_number = int(input('Введите номер оставшейся карточки: '))
    lost_card -= card_number
print('Потеряна карточка с номером:', lost_card)



