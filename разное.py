n = int(input())
m = [0]*80
a=b=0
for i in range(n):
    x = int(input())
    y = m[(80-x%80)%80]
    if y*x > a*b:
        a,b=x,y
    if x > m[x%80]:
        m[x%80] = x
print(a,b)