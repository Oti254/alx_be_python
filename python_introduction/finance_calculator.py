month_income = int(input("Enter your monthly income: "))
month_expense = int(input("Enter your monthly expenses: "))

#Calculating monthly savings
month_saving = month_income - month_expense

#projecting annual savings at 5%
projected_savings = int(month_saving * 12 + (month_saving * 12 * 0.05))

#Displaying monthly savings
print(f"Your monthly savings are ${month_saving}")

#Projected annual savings
print(f"Projected savings after one year, with interest, is: ${projected_savings}")

