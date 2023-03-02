# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

array = [0, -1, 5, 2, 3]

temp_str = ""

index = 0
num = array[0]
for i in array:
    if num < i:
        temp_str = temp_str + f"({num} < {i}) "
        num = i
        index += 1
    else:
        num = i

print(index, temp_str.replace(") (", ", "))
