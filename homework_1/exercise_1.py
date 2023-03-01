
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

# расчёты оплаты за электричество
a = (el_current - el_previous) * el_tariff
print(f'You need to pay for electricity {a}')
print(a)


# water
w_previous = 50
w_current = 126
w_tariff = 0.7
print(f'Previous water readings is {w_previous}')
print(f'Current water readings is {w_current}')
print(f'Water tariff is {w_tariff}')

# расчёты оплаты за воду
b = (w_current - w_previous) * w_tariff
print(f'You need to pay for water {round(b, 2)}')
print(round(b, 2))



# sum for water and electricity
c = a + round(b, 2)
print(f'All you need to pay for water and electricity {c}')
print(c)




