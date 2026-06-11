'''Constraints
• Use functions to modularize the program. 
• Use file handling (open(), read(), write(), append()). 
• Use lists/dictionaries wherever appropriate. 
• Do not use databases or external libraries. 
• Implement menu-driven execution using a while loop. 
• Ensure that updates are reflected in the original file.
5. Daily Expense Tracker and Report Generator
Problem Statement
Daily expenses are recorded in expenses.txt.
File Format
Food,450
Travel,300
Shopping,1200
Electricity,850
Internet,700
Entertainment,600
Medicine,400
Education,1500
Fuel,900
Miscellaneous,250
Requirements
Develop a program to:
1. Display all expenses. 
2. Calculate total expenditure. 
3. Find the category with highest and lowest spending. 
4. Display expenses greater than ₹800. 
5. Add a new expense category. 
6. Update an existing expense amount. 
7. Generate a summary report in report.txt containing: 
o Total Expenses 
o Highest Expense Category 
o Lowest Expense Category 
o Categories spending more than ₹800'''
print("--------------------------Daily Expense Tracker and Report Generator--------------------------")
#function to display all expenses
def display_expenses():
    with open("expenses.txt", "r") as file:
        for line in file:
            category, amount = line.strip().split(",")
            print(f"{category}: ₹{amount}")
#function to calculate total expenditure
def calculate_total_expenditure():
    total = 0
    with open("expenses.txt", "r") as file:
        for line in file:
            _, amount = line.strip().split(",")#splitting line by comma and assigning amount to variable
            total += int(amount)
    return total
#function to find the category with highest and lowest spending
def find_highest_lowest_spending():
    highest_spending = None
    lowest_spending = None
    with open("expenses.txt", "r") as file:
        for line in file:
            category, amount = line.strip().split(",")
            amount = int(amount)
            if highest_spending is None or amount > highest_spending[1]:#if highest spending is None or amount of category is greater than highest spending
                highest_spending = (category, amount)#update highest spending
            if lowest_spending is None or amount < lowest_spending[1]:
                lowest_spending = (category, amount)
    return highest_spending, lowest_spending
#function to display expenses greater than ₹800
def display_expenses_greater_than_800():
    with open("expenses.txt", "r") as file:
        for line in file:
            category, amount = line.strip().split(",")
            amount = int(amount)
            if amount > 800:
                print(f"{category}: ₹{amount}")
#function to add a new expense category
def add_expense_category():
    category = input("Enter the category: ")
    amount = int(input("Enter the amount: "))
    with open("expenses.txt", "a") as file:
        file.write(f"{category},{amount}\n")
#function to update an existing expense amount
def update_expense_amount():
    category = input("Enter the category: ")
    amount = int(input("Enter the new amount: "))
    with open("expenses.txt", "r") as file:
        lines = file.readlines()
    with open("expenses.txt", "w") as file:
        for line in lines:
            current_category, _ = line.strip().split(",")
            if current_category == category:
                file.write(f"{category},{amount}\n")
            else:
                file.write(line)
#function to generate a summary report
def generate_summary_report():
    total = calculate_total_expenditure()
    highest_spending, lowest_spending = find_highest_lowest_spending()
    with open("report.txt", "w") as report_file:
        report_file.write(f"Total Expenses: ₹{total}\n")
        report_file.write(f"Highest Expense Category: {highest_spending[0]}: ₹{highest_spending[1]}\n")
        report_file.write(f"Lowest Expense Category: {lowest_spending[0]}: ₹{lowest_spending[1]}\n")
        report_file.write("Categories spending more than ₹800:\n")
        with open("expenses.txt", "r") as expenses_file:
            for line in expenses_file:
                category, amount = line.strip().split(",")
                amount = int(amount)
                if amount > 800:
                    report_file.write(f"{category}: ₹{amount}\n")
#calling functions
display_expenses()
print("----------------------------------------------------------------")
calculate_total_expenditure()
print("----------------------------------------------------------------")
find_highest_lowest_spending()
print("----------------------------------------------------------------")
display_expenses_greater_than_800()
print("----------------------------------------------------------------")
add_expense_category()
print("----------------------------------------------------------------")
update_expense_amount()
print("----------------------------------------------------------------")
generate_summary_report()
