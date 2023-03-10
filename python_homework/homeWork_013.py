# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input("Введите число: "))
b = int(input("Введите степень: "))

def exponentiation(a, b):
    if b == 1:
        return a
    b -= 1
    return exponentiation(a, b) * a

print(exponentiation(a, b))
