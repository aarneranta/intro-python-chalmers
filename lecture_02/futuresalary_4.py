# file futuresalary_4.py

def final_amount(amount, increase, years):
    for y in range(1, years+1):
        amount = amount * (1 + increase/100)
    return amount


def main():
    salary = float(input("current salary: "))
    increase = float(input("yearly raise in percent: "))
    years = int(input("how many years ahead? "))   
    end_salary = final_amount(salary, increase, years)
    print('Final salary in year', years, ':', end_salary)


if __name__ == '__main__':
    main()

    
