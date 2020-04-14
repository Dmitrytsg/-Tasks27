N = int(input())
mPair = 0
m = 0
a = 0
b = 0
for i in range(N):
    x = int(input())
    if abs(x-m)%2 == 0 and (x%19 == 0 or m%19 == 0) and x + m > mPair:
            mPair = x + m
            a = x
            b = m
    if x > m:
        m = x
print(a,b)
