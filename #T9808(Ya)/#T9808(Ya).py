#основная идея в том что, при если a+b кратны 120,то a%120 + b%120 = 120,либо a%120 + b%120 = 0
max_by_residue = [0]*120 #массив для чисел,где каждая ячейкаа это остаток от 120,и в неё кладётся наибольшее число с таким остатком
n = int(input())
max_sum = 0 # задаём максимальную сумму
left,right = None,None
for i in range(n):
    m = int(input())
    residue_m = m%120
    mirror_residue = (120 - residue_m)%120 # т.к если residue_m = 0, то 120 - 0 = 120, а такого быть не может,т.е зеркальный 0 это только 0, (120-101)%120 = 19,так что ничего страшного
    m_best = max_by_residue[mirror_residue] #берём в массиве подходящий противоположный максимум
    if m_best != 0 and m_best > m and m + m_best > max_sum: #проверяем есть ли в массиве подходящий противоположный максимум,и т.к он шёл раньше то он должен быть больше m
        max_sum = m + m_best
        left = m_best
        right = m
    if m > max_by_residue[residue_m]:
        max_by_residue[residue_m] = m #обновляем максимум по данному остатку

print(left,right)
