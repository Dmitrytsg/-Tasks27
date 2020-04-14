N = int(input())
a = [0]*4
c3 = 0
cN3 = 0
count = 0
for i in range(4):
    a[i] = int(input())
for i in range(4,N):
    x = int(input())
    p = a[i%4]
    if p%3 == 0:
        c3 += 1
    else:
        cN3 += 1
    if x%3 == 0:
        count += cN3
    else:
        count += c3
    a[i%4] = x    
print(count)