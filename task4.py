"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
my_dict = {'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре'}
eng_file = open('task4_a.txt', 'r', encoding='UTF-8')
rus_file = open('task4_b.txt', 'w', encoding='UTF-8')
while True:
    line_eng = eng_file.readline().lower().split(' - ')
    if not line_eng[0]:
        break
    line_rus = [my_dict.get(line_eng[0]), line_eng[1]]
    rus_file.write(' - '.join(line_rus))
eng_file.close()
rus_file.close()
