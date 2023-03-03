# пользователь вводит строку
user_input = input(f'Please, input your string:')

u = user_input.lower()
u = user_input.strip('.')
u = user_input.strip(',')
u = user_input.strip('-')
u = user_input.strip(':')
u = user_input.strip(';')
u = user_input.strip('!')
u = user_input.strip('?')
u = user_input.rstrip()
print(u)

# пользователь выбирает слово, поиск слова в предложении
user = input(f'What do you want to replace?')
a = user_input.find(user)
print(f'"{user}" was found at position {a}')

# меняем на слово пользователя
user_repl = input(f'With what do you want to replace?')
b = user_input.replace(user, user_repl)
print(input(f'Here is your result:\n {b}'))




