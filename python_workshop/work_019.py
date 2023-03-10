# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, a = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
import time

num_fib = int(input("Введите порядковый номер числа Фибоначчи: "))
list1 = []

tic = time.perf_counter()
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(1, num_fib + 2):
    list1.append(fib(i))
    if num_fib + 1 == i:
         print(list1[i-1])

toc = time.perf_counter()
print(f"{toc - tic:0.4f}")

