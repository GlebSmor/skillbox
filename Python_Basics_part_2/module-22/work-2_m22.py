string_list = []
zen = open('work-2/zen.txt', 'r')
for line in zen:
    clear_line = line.rstrip()
    if clear_line:
        string_list.append(line)
zen.close()
for i in range(len(string_list) - 1, -1, -1):
    print(string_list[i])
    