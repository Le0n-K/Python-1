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

# диалог с пользователем

n = 0

el_previous = input("Enter your previous electricity readings:" )
print(f'Your previous readings is {el_previous}')

el_current = input("Enter your current electricity readings:")
print(f'Your current readings is {el_current}')

el_tariff = input("Enter your electricity tariff:")
print(f'Your tariff is {el_tariff}')

yes = input("Do you want to know your sum readings for electricity?")
yes = c
print(f'Your sum is {yes}')

no = input("Do you want to know your sum readings for electricity?")
no = n

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

i = 0

w_previous = input("Enter your previous water readings:" )
print(f'Your previous readings is {w_previous}')

w_current = input("Enter your current water readings:")
print(f'Your current readings is {w_current}')

w_tariff = input("Enter your water tariff:")
print(f'Your tariff is {w_tariff}')

yes = input("Do you want to know your sum readings for water?")
yes = round(f, 2)
print(f'Your sum is {yes}')

no = input("Do you want to know your sum readings for water?")
no = i

# sum for water and electricity

x = c + round(f, 2)
print(x)
print(f'All you need to pay for water and electricity {x}')

j = 0

yes = input("Do you want to know your sum readings for water and electricity?")
yes = x
print(f'Your sum is {yes}')

no = input("Do you want to know your sum readings for water and electricity?")
no = j

