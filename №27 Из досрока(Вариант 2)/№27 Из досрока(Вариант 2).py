N = int(input())
mPair = 0 #макисмальная сумма пары,которая динамический обновляется
m = -2 #максимальный элемент,который динамический обновляется
a = 0
b = 0
for i in range(N):
    x = int(input())
    if abs(x-m)%2 == 0 and (x%19 == 0 or m%19 == 0) and x + m > mPair: #все условия для пары
            mPair = x + m #обновляем сумму пары
            a = x #обновляем сами элементы
            b = m
    if x > m:#обновляем max элемент
        m = x
print(a,b)
