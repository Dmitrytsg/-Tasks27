N = 30
a = [int(input()) for i in range(N)]
m = 0
for i in a:
    if i%5 != 0 and i>m:
        m = i
for i in a:
    if i%5 != 0:
        i = m
    print(i)
