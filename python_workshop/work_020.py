# Написать функцию вычисления факториала числа n:

n = int(input("Введите число N!: "))

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(n))
