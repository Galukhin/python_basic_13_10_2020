"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
sum_salary = 0
cnt = 0
print('Сотрудники с окладом меньше 20 т.р.:')
with open('task3.txt', 'r', encoding='UTF-8') as my_file:
    while True:
        line = my_file.readline()
        if not line:
            break
        worker, salary = line.split()
        if float(salary) < 20000:
            print(worker)
        sum_salary += float(salary)
        cnt += 1
print(f'Средняя величина дохода: {sum_salary / cnt}')
