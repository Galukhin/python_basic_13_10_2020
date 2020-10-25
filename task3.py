"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
from my_module import my_range
result = [itm for itm in my_range(241, 20) if not itm % 20 or not itm % 21]
print('Результат:', result)
