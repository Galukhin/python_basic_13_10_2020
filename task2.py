"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
my_list = []
print("Добавьте что-нибудь в список. Для окончания нажмите q")
item = 0
while True:
    item = input(">>>")
    if item == "q":
        break
    my_list.append(item)

for i in range(len(my_list) // 2):
    my_list[i * 2], my_list[i * 2 + 1] = my_list[i * 2 + 1], my_list[i * 2]
print(my_list)
