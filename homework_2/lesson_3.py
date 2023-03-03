# пользователь вводит строку
user_input = input(f'Please, input your string:')
# пользователь пишет "Today is a RainY Day! do you like It? By the Way, i don't."
user_input = user_input.lower()
user_input = user_input.strip('.,-:;?!')
user_input = user_input.rstrip()
print(user_input)

# пользователь выбирает слово "day", поиск слова в предложении
user = input(f'What do you want to replace?')
a = user_input.find('day')
print(f'"Day" was found at position {a}')

# меняем на слово 'night'
user_repl = input(f'With what do you want to replace?')
b = user_input.replace('day', 'night')
print(input(f'Here is your result:\n {b}'))













