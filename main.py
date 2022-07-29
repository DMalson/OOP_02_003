
file_list =[]
#Подсчёт количества строк
for file_name in ['1.txt', '2.txt', '3.txt'] :
    file_list.append([file_name, len(open(file_name, 'r', encoding='utf-8').readlines())])

#Сортировка
sorted_list = sorted(file_list, key=lambda x: x[1])

#Запись итогового файла
with open('result.txt', 'w', encoding='utf-8') as target :
    for file_name, num_lines in sorted_list:
        target.write(file_name + '\n')
        target.write(str(num_lines) + '\n')
        with open(file_name, 'r', encoding='utf-8') as source :
            for line in source:
                target.write(line.strip('\n') + '\n')

