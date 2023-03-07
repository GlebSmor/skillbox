n = float(input())
a = 1
count = 0
while n > 10:
    n /= 10
    count += 1
print('x =', n, '* 10 **', count)