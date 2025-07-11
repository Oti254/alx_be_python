monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

#Calculating monthly savings
monthly_savings = monthly_income - monthly_expenses

#projecting annual savings at 5%
projected_savings = float(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

#Displaying monthly savings
print(f"Your monthly savings are ${monthly_savings:.0f}.")

#Projected annual savings
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")
