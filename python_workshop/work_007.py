'''
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
'''
num = int(input("введите число: "))

fib1 = 0
fib2 = 1
fib = 0
x = True
i = 2
while x:
    if num == 0:
        print(f"Число {num} находится на позиции {1}")
        x = False
    elif num == 1:
        print(f"Число {num} находится на позиции {2}")
        x = False
    elif fib > num:
        print("Нет числа")
        x = False
    elif fib == num:
        print(f"Число {num} находится на позиции {i}")
        x = False
    else:
        print(fib)
    
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    i = i + 1
    
    