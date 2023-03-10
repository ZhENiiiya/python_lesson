# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

count = int(input("Введите количество оценок: "))
list_1 = []
def max_to_min(count, lv):
    if count == 0:
        return lv

    estimation = int(input("Введите оценку -> "))
    
    if estimation > 3:
        estimation = 1
        lv.append(estimation)
    else:
        lv.append(estimation)
    
    return max_to_min(count - 1, lv)

print(max_to_min(count, list_1))
