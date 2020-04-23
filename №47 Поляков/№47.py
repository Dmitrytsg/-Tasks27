n = int(input())
minpx = float('+inf')
maxpx = 0
minnx = float('+inf')
maxnx = 0
maxpy = 0
maxny = 0
s = 0
for i in range(n):
    x,y = map(int,input().split())
    if x > 0:
        if y == 0:
            if x < minpx:
                minpx = x
            if x > maxpx:
                maxpx = x
        elif abs(y) > maxpy:
                maxpy = abs(y)
    elif x < 0:
        if y == 0:
            if abs(x) < minnx:
                minnx = abs(x)
            if abs(x) > maxnx:
                maxnx = abs(x)
        elif abs(y) > maxny:
                maxny = abs(y)
s = ((maxpx - minpx)*maxpy)*0.5
if s < ((maxnx - minnx)*maxny)*0.5:
    s = ((maxnx - minnx)*maxny)*0.5
print(s)