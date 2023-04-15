films_list = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
qty = int(input('Сколько фильмов хотите добавить? '))
fav_films = []
for films_num in range(qty):
    film = input('Введите название фильма: ')
    if film not in films_list:
        print('Ошибка: фильма', film, 'у нас нет :(')
    else:
        fav_films.append(film)

print('Ваш список любимых фильмов:', fav_films)
