# Написать функцию для нахождения наибольшего общего делителя двух чисел:

def nod(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return nod(b, a%b)

print(nod(99, 100))
