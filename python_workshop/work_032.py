# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# "1. Отобразить весь справочник\n"
# "2. Найти абонента по фамилии\n"
# "3. Найти абонента по номеру телефона\n"
# "4. Добавить абонента в справочник\n"
# "5. Сохранить справочник в текстовом формате\n"
# "6. Закончить работу")


fields = ["Фамилия", "Имя", "Номер", "Описание"]

def read_txt(filename: str) -> list: # Чтение справочника  
    data = []                        
    with open(filename, 'r', encoding="utf=8") as file: 
        for line in file:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def add_data(data:list): # Добавить абонента в справочник
    new_data = []
    for i in fields:
        new_data.append(input(f"Введите {i} -> "))
    record = dict(zip(fields, new_data))
    data.append(record)
    return data

def write_txt(filename:str, data:list): # Сохранить справочник в текстовом формате 
    with open(filename, 'r+', encoding="utf=8") as file:
        for i in data:
            for j in fields:
                x = i.get(j)
                file.write(f"{x}, ")
            file.write('\n')

def print_data(data:list): # Вывести весь справочник
    x = str
    for i in data:
        for j in fields:
           x = i.get(j)
           print(x, end=",")
        print()

def get_search_number(data:list, number): # Поиск по номеру
    x = str
    for i in data:
        number_list = int(i.get("Номер"))
        if number == number_list:
            for j in fields:
                x = i.get(j)
                print(x, end=",")
            print()

def get_search_lastname(data:list, lastname):
    x = str
    for i in data:
        lastname_list = str(i.get("Фамилия"))
        if lastname == lastname_list:
            for j in fields:
                x = i.get(j)
                print(x, end=",")
            print()


def menu():
    while True:
        x = int(input("Введите номер операции:\n"
                      "1. Отобразить весь справочник\n" 
                      "2. Найти абонента по фамилии\n"
                      "3. Найти абонента по номеру телефона\n"
                      "4. Добавить абонента в справочник\n"
                      "5. Сохранить справочник в текстовом формате\n"
                      "6. Закончить работу\n-> "))
        if x == 6:
            exit()
        elif x == 1:
            print("==============")
            print_data(read_txt("python_workshop\phone.txt"))
            print("==============")
        elif x == 2:
            lastname = str(input("Введите Фамилию абонента -> "))
            print("==============")
            get_search_lastname(read_txt("python_workshop\phone.txt"), lastname)
            print("==============")
        elif x == 3:
            number = int(input("Введите номер абонента -> "))
            print("==============")
            get_search_number(read_txt("python_workshop\phone.txt"), number)
            print("==============")
        elif x == 4:
           data = add_data(read_txt("python_workshop\phone.txt"))
        elif x == 5:
            write_txt("python_workshop\phone.txt", data)
        else:
            exit()

menu()