def create_list(n):
    x_list = []
    for i in range(n):
        number_list = int(input(f"Введите значение элемента {i} -> "))
        x_list.append(number_list)
    return x_list
    