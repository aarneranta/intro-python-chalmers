# file futuresalary_1.py

salary = 21000
increase = 2
years = 5   

for y in range(1, years+1):
    salary = salary * (1 + increase/100)
    print("year ", y, ":",salary)

