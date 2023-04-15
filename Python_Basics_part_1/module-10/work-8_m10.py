height = int(input('Введите высоту пирамиды: '))
for row in range(height):
    for col in range(height * 2 + 1):
        if -row + (height + 1) <= col <= row + (height + 1):
            print('#', end='')
        else:
            print(' ', end='')
    print()
  