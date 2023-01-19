print('this program calculates your remaining money')

salary = int(input('Tell me your salary '))
taxrate = int(input('Tell me your tax rate '))
rent = int(input('Tell me your rent '))

tax = salary * (taxrate/100)

remain = salary - tax - rent

print('your remaining income is ', remain)

