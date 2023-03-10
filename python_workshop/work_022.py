# Написать функцию для нахождения суммы цифр числа:

def sum_num(n):
    if n // 10 == 0:
        return n % 10
    return sum_num(n // 10) + n % 10

print(sum_num(55555))