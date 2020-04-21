N = int(input())
m=m2=mp=mp2=0
p = 19
for i in range(N):
    x = int(input())
    if x%2 == 0:
        if x%p == 0 and x > mp2:
            if mp2 > m2: 
                m2 = mp2 #таким образом самые максимальные чётные будут храниться в ячейках m2 и mp2
            mp2 = x
        elif x > m2:
            m2 = x
    else:
        if x%p == 0 and x > mp:
            if mp > m:
                m = mp #таким образом самые максимальные нечётные будут храниться в ячейках m и mp
            mp = x
        elif x > m:
            m = x
if m2*mp2 != 0 and (m2+mp2) > (m + mp):
    a,b = m2,mp2
elif mp*m != 0:
    a,b = m,mp
else:
    a,b=0,0
print(a,b)