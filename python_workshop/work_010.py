# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

number_list = [1, 1, 2, 0, -1, 3, 4, 4]

number_list2 = set(number_list)

print(number_list,"\n", len(number_list2))
