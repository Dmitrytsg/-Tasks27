d = 9 
a = [0]*(d) #stack для чисел чтобы расстояние было всегда 9
pr = -1 #максимальное произведение
mEven = -1
m = -1
N = int(input())
for i in range(d):#забиваем stack первыми d значениями
    a[i] = int(input())
for i in range(d,N): #работаем с след. числами
    x = int(input())
    index = a[i%d] #значение в stack расположенное не менее чем в 9 от x,как раз i%d покажет индекс 
    if index % 2 == 0 and index > mEven: #если значение чёт. и больше чёт-максимума, то обновляем max
        mEven = index 
    if index > m: #тут просто обновляем значение макс,тут максимум и чётый и нечётный
        m = index
    if x % 2 != 0: #нечётный x спариваем только с чётным максимумом и обновляем pr, если оно оказалось меньше
        if x*mEven > pr:
            pr = x*mEven
    elif x*m > pr: #чётный с любым
        pr = x*m
    a[i%d] = x #оперативно обнновляем stack,данный x побудет в роли index когда придёт его очередь
print(pr)
