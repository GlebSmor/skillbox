import os

file = open('../Python_Basic/Module22/07_tournament/first_tour.txt', 'r')
file_list = []
players_dict = {}
sorted_dict = {}
for line in file:
    line = line.strip(os.linesep)
    file_list.append(line.split())

for i_element in range(1, len(file_list)):
    if int(file_list[i_element][2]) > int(file_list[0][0]):
        file_list[i_element][1] = file_list[i_element][1][:1] + '. '
        players_dict[file_list[i_element][1] + file_list[i_element][0]] = int(file_list[i_element][2])

sorted_keys = sorted(players_dict, key=players_dict.get, reverse=True)

for elem in sorted_keys:
    sorted_dict[elem] = players_dict[elem]

new_file = open('second_tour.txt', 'w')
count = 0
new_file.write(f'{str(len(sorted_dict))}\n')

for k, v in sorted_dict.items():
    count += 1
    new_file.write(f'{count}) {k} {v}\n')
