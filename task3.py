# Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.


def SumElements (n):
    result = 0
    for i in range(1, n + 1):
        lst[i] = round((1 + 1/i)**i, 5)
        result = result + (1 + 1/i)**i
    print(lst)
    return result

n = int(input('Введите N: '))
lst = {}
print(round(SumElements(n), 5))