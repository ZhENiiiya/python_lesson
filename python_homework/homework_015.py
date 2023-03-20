# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: 
# a(n) = a(1) + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def progression(start:int, step:int, quantity:int):
    res = []
    temp = start
    for i in range(quantity):    
        res.append(temp)
        temp += 2
    return res

a = int(input("С какого числа начать: "))
b = int(input("Шаг: "))
c = int(input("Количество: "))

print(progression(a, b, c))
