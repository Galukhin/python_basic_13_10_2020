"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
user_time = int(input("Введите время в секундах:\n"))
hours = user_time//3600
user_time %= 3600
minutes = user_time//60
user_time %= 60
seconds = user_time
print(f"{hours:02d}", f"{minutes:02d}", f"{seconds:02d}", sep=":")
