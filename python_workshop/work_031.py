# Написать функцию, которая принимает список строк и 
# возвращает список строк, содержащих только одно слово, 
# с использованием лямбда-функции:

strings = ["hello world", "write", "qwerty qwerty"]

strings1 = list(filter(lambda x: len(x.split()) == 1, strings))
print(strings1)