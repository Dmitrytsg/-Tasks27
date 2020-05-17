N = int(input())
stacklen = 8
stack = [0]*stacklen
count = 0 #кол-во пар сумма кратна 8
m = [0]*8 #массив остатков
for i in range(8):
    x = int(input())
    mirror_resid = (8-x%8)%8
    count += m[mirror_resid] #подсчёт пар кратных 8
    m[x%8] += 1
    stack[i] = x
all_ = ((1+(stacklen-1))*(stacklen-1))//2 #кол-во пар для данного сдвига стека 
for i in range(8,N):
    all_ += stacklen - 1 #подсчитывая пары для нового сдвига,нельзя учитывать те,что уже были 
#сдвигаем стек!!!!!!!!!!!
    m[stack[0]%8] -= 1 
    del stack[0] 
#!!!!!!!!!!!!!!!!
    x = int(input())
    mirror_resid = (8-x%8)%8
    count += m[mirror_resid] #подсчёт пар кратных 8
    m[x%8] += 1
    stack.append(x)
print(all_ - count) #выводим кол-во пар не кратных 8