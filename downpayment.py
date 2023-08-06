total_cost = float(input('Enter total cost of home: '))
portion_down_payment = float(input('Enter portion of total price for down payment: '))
r = float(input('Enter expexted rate of return for investment: '))
semi_annual_raise = float(input('Enter semi annual raise: '))
annual_salary = float(input('Enter annual salary: '))
time = int(input('In how many months do you want to pay down payment?: '))

down_payment = portion_down_payment*total_cost

#calculates current_savings based on portion_saved determined from bisection
def calculate_current_savings(portion_saved):
    monthly_salary = annual_salary/12
    current_savings = 0
    for month in range(time):
        if month % 6 == 0 and month != 0: #raise every 6 months
            monthly_salary += monthly_salary * semi_annual_raise
        current_savings += current_savings*r/12 + monthly_salary*portion_saved
    return current_savings

if calculate_current_savings(1) >= down_payment: #checks to see if you can afford downpayment by saving 100% of salary
    epsilon = 100
    low = 0
    high = 1
    portion_saved = (low + high)/2
    num_guesses = 0

    while abs(calculate_current_savings(portion_saved)-down_payment) >= epsilon: #loop ends once you are 100$ within price of downpayement
        if calculate_current_savings(portion_saved) > down_payment:
            high = portion_saved
        else:
            low = portion_saved
        portion_saved = (low + high)/2
        num_guesses += 1
    
    print('you should save',str(round((portion_saved*100),2))+'%','of your monthly salary')
else:
    print('It is not possible to pay the down payment in given amount of time')