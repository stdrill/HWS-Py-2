# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input('Введите число: '))
lst = []
f = 1
for i in range(n):
    f = f * (i + 1)  
    lst.append(f)
print(lst)