# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "}, {" VIII":" S007 "}]
out_set = set()
print(list_dict, "\n")

for i in range(len(list_dict)):
    temp_dict = list_dict[i]
    for key in temp_dict.keys():
        x = temp_dict.get(key)
        out_set.add(x.replace(" ", ""))

print(out_set)