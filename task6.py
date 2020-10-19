"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара
и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
product_list = []
key_param = ["Название", "Цена", "Количество", "ед."]
cnt_tuple = 0
print("Заполнение структуры данных Товары")
while True:
    cnt_tuple += 1
    dict_param = {}
    for key in key_param:
        if key == "Цена" or key == "Количество":
            while True:
                value_param = input(f"Введите {key}: ")
                if value_param.isdigit():
                    break
                print(f"Параметр {key} должен быть числом!")
        else:
            value_param = input(f"Введите {key}: ")
        dict_param.update({key: value_param})
    product_list.append((cnt_tuple, dict_param))
    answer = input("Продолжить заполнение?\ny - да, n - нет >>>")
    if answer == "n":
        break
for item in product_list:
    print(item)
print("*" * 20)

dict_analytic = {}
for key in key_param:
    value_list = []
    for item in product_list:
        value_list_item = item[1].get(key)
        value_list.append(value_list_item)
    value_list = list(set(value_list))
    dict_analytic.update({key: value_list})
for key, value in dict_analytic.items():
    print(f"{key}: {value}")
