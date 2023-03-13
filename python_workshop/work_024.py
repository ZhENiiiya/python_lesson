# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
def create_list(n):
    x_list = []
    for i in range(n):
        number_list = int(input(f"Введите значение элемента {i} -> "))
        x_list.append(number_list)
    return x_list
        
def create_ex_list(x:list, y:list):
    new_list = []
    for i in x:
        if i not in y:
            new_list.append(i)
    return new_list


n = int(input("Задайте количество элементов списка N: "))
list_1 = create_list(n)

m = int(input("Задайте количество элементов списка M: "))
list_2 = create_list(m)

new_list = create_ex_list(list_1, list_2)

print(new_list)
