N = int(input())
b = [0]*101
j = 0
for i in range(N):
    x = int(input())
    b[x] += 1
    print(b)
N //= 2
while N >= b[j]:
        N -= b[j]
        j += 1
        print(N,j)
print(j)