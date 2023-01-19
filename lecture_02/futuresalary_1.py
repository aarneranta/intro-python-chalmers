# file futuresalary_1.py

amount = 21000
for y in range(1, 6):
    amount = amount * (1 + 2/100)
    print("year", y, ":", amount)


