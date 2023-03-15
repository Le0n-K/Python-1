i = 0

while True:
    user_input = input("Введіть число або sum для отримання підсумку: ")

    if user_input == "sum":
        break  # вихід з циклу, якщо користувач ввів "sum"

    try:
        number = float(user_input)  # перетворюємо введене значення на число
    except ValueError:
        print("Некоректне введення! Введіть число або sum, будь-ласка.")
    else:
        i += number  # додамо число до підсумку, якщо введення коректне

print(f"Підсумок: {i}")
