"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
print("Решение через list")
months = ["12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
seasons = ["Зима", "Весна", "Лето", "Осень"]
while True:
    user_month = input("Введите номер месяца\n")
    if user_month in months:
        break
    print("Месяца с таким номером не существует, введите еще раз")
result_season = seasons[months.index(user_month) // 3]
print(f"{user_month}-й месяц относится к времени года: {result_season}")

print("*"*10, "\nРешение через dict")
months = ["12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
seasons = ["Зима", "Весна", "Лето", "Осень"]
my_dict = {}
for item in months:
    my_dict.update({item: seasons[months.index(item) // 3]})
while True:
    user_month = input("Введите номер месяца\n")
    if user_month in months:
        break
    print("Месяца с таким номером не существует, введите еще раз")
result_season = my_dict.get(user_month)
print(f"{user_month}-й месяц относится к времени года: {result_season}")
