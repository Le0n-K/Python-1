i = 0

while True:
    user_input = input("Введіть число: ")
    if user_input == "sum":
        print(i)
        break
    else:
        try:
            i += float(user_input)
        except ValueError:
            print("Некоректне введення! Введіть число або 'sum' для підсумовування.")
