"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""
user_digit = input("Введите число от 1 до 9:\n")
number1 = user_digit * 3
number2 = user_digit * 2
result = int(user_digit) + int(number2) + int(number1)
print("Результат:", result)
