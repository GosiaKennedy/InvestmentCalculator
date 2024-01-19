import math

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on home loan.")

chosen_option = input("Enter either 'investment' or 'bond' from the menu above to proceed:").lower()

if chosen_option == "investment":
    deposit = float(input("Enter the amount of your deposit, as a number:"))
    interest_rate = int(input("Enter the interest rate as a number, omitting percentage sign:"))
       # divides the amount by 100
    interest_rate /=100 
    
    investment_length = int(input("Enter the investment length in years:"))
    interest = input("Enter the type of interest you're interested in: simple or compound:")
    if interest == "simple": 
            total_amount = deposit*(1 + interest_rate*investment_length)
    elif interest == "compound":
            total_amount = deposit * math.pow((1 + interest_rate), investment_length)
    print(f"You will receive £{total_amount} in total")
elif chosen_option == "bond":
    house_value = float(input("Enter the present value of the house:"))
    interest_rate = int(input ("Enter the interest rate as a number, omitting the percentage sign:"))
    repayment_length = int(input ("Enter the repayment length in months:"))
    monthly_interest = float(interest_rate/100/12) 
    repayment = (monthly_interest*house_value)/(1-(1+monthly_interest)**(-repayment_length))
    print(f"You will have to repay £ {repayment} each month.")

else:
    message = input("This is not a valid input. Enter either 'bond' or 'investment' to proceed:")
    
    