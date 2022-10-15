# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

def MultiplicationElements (lst, lstposition):
    res = 1
    for i in lstposition:
        res = res * lst[int(i)]
    return res


n = int(input('Enter N: '))
lst = []
for i in range(n):
    num = random.randint(-n, n)
    lst.append(num)
print(lst)

with open('task4.txt', 'r') as my_file:
    data = my_file.read()
lstposition = data.split()
print(lstposition)
int(lstposition[0])

print(MultiplicationElements(lst, lstposition))