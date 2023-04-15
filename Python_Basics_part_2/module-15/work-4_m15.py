qty = int(input('Количество видеокарт: '))
gpu_list = []
new_gpu_list = []
for gpu_num in range(1, qty + 1):
    video_card = int(input(f'{gpu_num} Видеокарта: '))
    gpu_list.append(video_card)
newest = gpu_list[0]
for newest_gpu in range(len(gpu_list)):
    if gpu_list[newest_gpu] > newest:
        newest = gpu_list[newest_gpu]
for gpu in gpu_list:
    if gpu != newest:
        new_gpu_list.append(gpu)
print('Старый список видеокарт:', gpu_list)
print('Новый список видеокарт:', new_gpu_list)
