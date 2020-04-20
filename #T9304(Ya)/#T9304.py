N = int(input())
stack = [0]*4 #очередь
resid = [0]*3 #массив остков при делении на 3
count = 0 
for i in range(4):
    stack[i] = int(input()) #запоняем очередь
for i in range(4,N):
    x = int(input())
    resX = x%3 #ост. от при x/3
    p = stack[i%4] #берём эл. из стека
    res = p%3 #ост. при p/3
    resid[res] += 1 #обновляем массив остатков
    if resX == 0: #если x кратен 3, то прибавляем все числа с остатками не 0(чтобы сумма не делилась на 3)
        count += resid[1] + resid[2]
    else:
        count += resid[0] #иначе прибавляем,только все числа кратные трём
    stack[i%4] = x    
print(count)