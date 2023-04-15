nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

unwrapped_list = [nice_list[a][b][c] for a in range(len(nice_list))
                  for b in range(len(nice_list[a]))
                  for c in range(len(nice_list[a][b]))]

print('Ответ:', unwrapped_list)