print("Welcome to Personal Budget Calculator")

# Input income
income = float(input("Enter your monthly income: "))

# Input expenses
print("Enter your expenses for the following categories:")
food_expense = float(input("Food: "))
rent_expense = float(input("Rent: "))
entertainment_expense = float(input("Entertainment: "))
utilities_expense = float(input("Utilities: "))
other_expense = float(input("Others: "))

# Calculate total expenses
total_expenses = food_expense + rent_expense + entertainment_expense + utilities_expense + other_expense

# Calculate savings
savings = income - total_expenses

# Display summary
print("\n----- Budget Summary -----")
print("Monthly Income: $", income)
print("Total Expenses: $", total_expenses)
print("    Food: $", food_expense)
print("    Rent: $", rent_expense)
print("    Entertainment: $", entertainment_expense)
print("    Utilities: $", utilities_expense)
print("    Others: $", other_expense)
print("Savings: $", savings)
print("---------------------------")
