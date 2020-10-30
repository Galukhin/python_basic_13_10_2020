"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
str_num = 0
my_list = []
with open('task2.txt', 'r', encoding='UTF-8') as my_file:
    while True:
        line = my_file.readline()
        if not line:
            break
        str_num += 1
        my_list.append(len(line.split()))
print(f'Количество строк: {str_num}\nКоличество слов в каждой строке:')
for idx, itm in enumerate(my_list, 1):
    print(f'{idx}: {itm}')
