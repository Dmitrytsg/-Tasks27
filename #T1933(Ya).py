N = int(input())
s = 4
count = 0
for i in range(N):
        m = int(input())
        if m % 29 == 0:
            for j in range(N-1):
                if abs(i - j) >= s:
                    count += 1  
                              
print(count)