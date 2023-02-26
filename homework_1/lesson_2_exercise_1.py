import math
import time

# Написати програму, що рахує абонплату за комунальним лічильника (наприклад, електроенергії або газу).
# Вхідні дані:
# попередні показання
# теперішні показання
# тариф.
# На виході:
# скільки потрібно сплатити, округлено до двох цифр після коми

# electricity

el_previous = 37
el_current = 54
el_tariff = 2.5
print(f'Previous electricity readings is {el_previous}')
print(f'Current electricity readings is {el_current}')
print(f'Electricity tariff is {el_tariff}')

a = el_tariff * el_previous   # предыдущие показатели электроэнергии по тарифу
print(a)

b = el_tariff * el_current    # текущие показатели электроэнергии по тарифу
print(b)

c = a + b    # сумма предыдущих и текущих показателей электроэнергии
print(c)
print(f'Sum for electricity is {c}')


# water

w_previous = 50
w_current = 126
w_tariff = 0.7
print(f'Previous water readings is {w_previous}')
print(f'Current water readings is {w_current}')
print(f'Water tariff is {w_tariff}')

d = w_tariff * w_previous    # предыдущие показатели воды по тарифу
print(d)

e = w_tariff * w_current     # текущие показатели воды по тарифу
print(e)
print(round(e, 2))

f = d + e     # сумма предыдущих и текущих показателей воды
print(f)
print(round(f, 2))
print(f'Sum for water is {round(f, 2)}')

# sum for water and electricity

x = c + f
print(x)
print(f'All you need to pay for water and electricity {x}')