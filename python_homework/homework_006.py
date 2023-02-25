# Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

s = int(input("Задайте сумму чисел: "))
p = int(input("Задайте произведение чисел: "))

x = 0
y = 0

for i in range(1000):
    for j in range(1000):
        if j + i == s and j * i == p:
            x = j
            y = i

print(f"Были загаданы числа {x} и {y}")