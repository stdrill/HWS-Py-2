# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

def SumDigits(n):
    sum = 0
    while (n !=0):
        sum = sum + n % 10
        n = n // 10
    return sum

num = float(input('Введите число: '))
sum = SumDigits(num)
print(round(sum))