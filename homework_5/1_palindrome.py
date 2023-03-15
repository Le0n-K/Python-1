def is_palindrome(input_str):
    # Переводимо строку в нижній регістр і видаляємо зайві символи
    input_str = input_str.lower().replace(" ", "").replace("\n", "").replace("\t", "").replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "").replace("-", "").replace("_", "").replace("(", "").replace(")", "")
    # Порівнюємо вихідну строку з її реверсом
    return input_str == input_str[::-1]

# Приклад використання
while True:
    input_str = input("Введіть строку: ")
    if is_palindrome(input_str):
        print("Це паліндром")
        break      # тут можна і без брейку, але це буде без кінця, тому на палідромі виходимо з циклу
    else:
        print("Це не паліндром")
