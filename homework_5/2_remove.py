def remove_parentheses(string):
    while "(" in string and ")" in string:
        start = string.index("(")
        end = string.index(")", start)
        string = string[:start] + string[end + 1:]
    return string


input_string = input("Введіть строку: ")
output_string = remove_parentheses(input_string)
print("Результат: ", output_string)
