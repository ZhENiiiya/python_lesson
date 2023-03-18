# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:          Вывод:
# 1 2 3 2 3      2

array = [3,3,3]

def identical_elements(arr: tuple):
    count = 0
    num_del = 1
    for i in range(len(arr)):
        num_x = arr[i]
        for j in range(num_del, len(arr)):
            if num_x == arr[j]:
                count += 1
                num_del +=1
    return count // 2
 
print(identical_elements(array))
