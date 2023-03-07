films_list = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
qty = int(input('Сколько фильмов хотите добавить? '))
fav_films = []

for films_num in range(qty):
    film = input('Введите название фильма: ')
    for check_film in films_list:
        if check_film == film:
            fav_films.append(film)
            check = True
    if not check:
        print('Ошибка: фильма', film, 'у нас нет :(')
    check = False
print('Ваш список любимых фильмов:', fav_films)

