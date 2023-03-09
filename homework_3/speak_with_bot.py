while True:
    # зчитування звернення користувача
    user_input = input('Введіть ваше повідомлення: ').lower()

    # пошук ключових слів та відповіді на них
    if 'привіт' in user_input or 'хеллоу' in user_input or 'хай' in user_input or 'доброго дня' in user_input:
        print('Вітаю, я бот з України!')
    elif 'що робиш' in user_input or 'як справи' in user_input or 'чим займаєшься' in user_input:
        print('Вчусь спілкуватись з людьми) А ви?')
    elif 'фільм' in user_input or 'серіал' in user_input or 'кіно' in user_input:
        print('Якщо вам буде цікаво - можу порадити вам подивитися новий фільм Мій сусід Отто дуже крутий!')
    elif 'бувай' in user_input or 'до зустрічі' in user_input or 'на все добре' in user_input or 'щасти' in user_input:
        print('Бажаю успіхів! До скорої зустріч:)')
        exit()
    else:
        print('Дуже цікаво, але, нажаль, нічого не зрозуміло :(')
