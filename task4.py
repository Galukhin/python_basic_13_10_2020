"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
user_number = int(input("Введите целое положительное число "))
max_digit = 0
while user_number > 0:
    if user_number % 10 > max_digit:
        max_digit = user_number % 10
    user_number = user_number // 10
print("Самая большая цифра в числе: ", max_digit)
