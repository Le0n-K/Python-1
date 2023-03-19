user_income = float(input('Введите свой доход: '))
user_tax = float(input('Введите ваш налог: '))

def sum_tax(comment):
    while True:
        try:
            sum_tax = (user_income / 100) * user_tax
            return float(sum_tax)
        except Exception:
            print('Введите число!')


def net_income (comment):
    while True:
        try:
            net_income = user_income - sum_tax
            return float(net_income)
        except Exception:
            print('Введите число!')