N = int(input())
max19 = 0
max219 = 0
max2 = 0
maxN = 0
a,b = 0,0
for i in range(N):
    x = int(input())
    if x%38 == 0:
            if x + max2 > a + b:
                        a = x
                        b = max2
            elif x + max219 > a + b:
                        a = x
                        b = max219    
            if x > max219:
                        max219 = x
    elif x%19 == 0:
            if x + maxN > a + b:
                        a = x
                        b = maxN
            elif x + max19 > a + b:
                        a = x
                        b = max19 
            if x > max19:
                        max19 = x
    elif x%2 == 0:
            if x + max219 > a + b:
                        a = x
                        b = max219  
            if x > max2:
                        max2 = x 
    else:
            if x + max19 > a + b :
                        a = x
                        b = max19
            if x > maxN:
                        maxN = x
if a*b == 0: 
        a = 0
        b = 0
print(a,b)