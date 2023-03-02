import math

income = 18000
print(f'Доход составляет {income} uah')

tax = 1200 / 100
print(f'Процент налога составляет {tax} %')

# вычисления объема налога
a = (income / 100) * tax
print(f'Сумма оплаты налога равна {a} uah')

# вычисления чистого налога
b = income - a
print(f'Чистый доход равен {b} uah')
