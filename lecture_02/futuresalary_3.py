# file futuresalary_3.py

salary = int(input("current salary: "))
increase = float(input("yearly raise in percent: "))
years = int(input("how many years ahead? "))   

for y in range(1, years+1):
    salary = salary * (1 + increase/100)
    print("year",y,":",salary)
