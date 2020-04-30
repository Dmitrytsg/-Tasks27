"""Данный алгоритм работает только для чисел < 10000(соответсвтует у-ю)"""
N = int(input())
m = [0]*100 #массив максимумов с соответствующими последними цифрами
max_sum = 0
for i in range(N):
    x = int(input())
    d = x%100
    if d > 2:
        mirror_d = (112 - d)%100 #вычисляем противоположные последние цифры 
        if x < m[mirror_d] and x + m[mirror_d] > max_sum:
            max_sum = x + m[mirror_d]
        if x > m[d]:
            m[d] = x
print(max_sum)

    