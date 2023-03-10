#  В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

blueberry_bushes = [3, 6, 7, 9, 2, 10]
rez = 0
maximum = 0
if len(blueberry_bushes) == 3:
    for i in blueberry_bushes:
        rez += i
elif len(blueberry_bushes) > 3:
    for i in range(2, len(blueberry_bushes) - 1):
        rez = blueberry_bushes[i - 1] + blueberry_bushes[i] + blueberry_bushes[i + 1]
        if rez > maximum:
            maximum = rez
print(maximum)

#########################################
# Правильный вариант ####################
blueberry_bushes = [12, 6, 7, 9, 10, 10]
rez = 0
maximum = 0
if len(blueberry_bushes) == 3:
    for i in blueberry_bushes:
        rez += i
elif len(blueberry_bushes) > 3:
    for i in range(len(blueberry_bushes)):
        rez = blueberry_bushes[i - 2] + blueberry_bushes[i - 1] + blueberry_bushes[i]
        if rez > maximum:
            maximum = rez
print(maximum)
