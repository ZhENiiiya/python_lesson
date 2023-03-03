# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

# Что-то увлёкся

n = int(input("Введите размер массива: "))
array_str = input("Введите значения для массива: ").replace(" ", "")
x = int(input("Введите число для поиска ближайшего числа: "))

nearest_numbers = set()
array = []

if n > len(array_str):
    print("Количество элементов не соответствует размеру массива.")
elif n < len(array_str):
    flag = input("Количество элементов не соответствует размеру массива. Не все значения будут сохранены. Заполнить массив? (y or n): ")
    if flag == "y" or flag == "Y":
        for i in range(n):
            if x - 1 == int(array_str[i]):
                nearest_numbers.add(int(array_str[i]))
            elif x + 1 == int(array_str[i]):
                nearest_numbers.add(int(array_str[i]))
            array.append(int(array_str[i]))
        array.sort()
        if x not in array and x < array[0]:
            nearest_numbers.add(array[0])
        elif x not in array and x > array[len(array) - 1]:
            nearest_numbers.add(array[len(array) - 1])
    else:
        exit()
else:
    for i in range(n):
        if x - 1 == int(array_str[i]):
            nearest_numbers.add(int(array_str[i]))
        elif x + 1 == int(array_str[i]):
            nearest_numbers.add(int(array_str[i]))
        array.append(int(array_str[i]))
    array.sort()
    if x not in array and x < array[0]:
        nearest_numbers.add(array[0])
    elif x not in array and x > array[len(array) - 1]:
        nearest_numbers.add(array[len(array) - 1])

print(nearest_numbers)
