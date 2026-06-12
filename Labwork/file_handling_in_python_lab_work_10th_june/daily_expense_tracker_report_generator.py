'''5. Daily Expense Tracker and Report Generator 
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
o Categories spending more than ₹800 '''
print("------------------ Daily Expense Tracker and Report Generator ------------------")

# Function to display all expenses
def display_expenses():
    print("\n1. Display All Expenses")
    with open("expenses.txt", "r") as file:
        for line in file:
            #Skip empty lines
            if line.strip():

                # Split category and amount
                category, amount = line.strip().split(",")

                print(f"{category}: Rs.{amount}")


# Function to calculate total expenditure
def calculate_total_expenditure():

    total = 0

    with open("expenses.txt", "r") as file:

        for line in file:

            if line.strip():

                # Extract amount only
                _, amount = line.strip().split(",")

                total += int(amount)

    return total


# Function to find highest and lowest spending category
def find_highest_lowest_spending():

    highest_spending = None
    lowest_spending = None

    with open("expenses.txt", "r") as file:

        for line in file:

            if line.strip():

                category, amount = line.strip().split(",")

                amount = int(amount)

                # Check highest expense
                if highest_spending is None or amount > highest_spending[1]:
                    highest_spending = (category, amount)

                # Check lowest expense
                if lowest_spending is None or amount < lowest_spending[1]:
                    lowest_spending = (category, amount)
    print("Highest =", highest_spending)
    print("Lowest =", lowest_spending)

    return highest_spending, lowest_spending


# Function to display expenses greater than ₹800
def display_expenses_greater_than_800():

    print("\n4. Expenses Greater Than ₹800")

    with open("expenses.txt", "r") as file:

        for line in file:

            if line.strip():

                category, amount = line.strip().split(",")

                amount = int(amount)

                if amount > 800:
                    print(f"{category}: Rs.{amount}")


# Function to add a new expense category
def add_expense_category():

    print("\n5. Add New Expense Category")

    category = input("Enter Category Name: ")

    amount = int(input("Enter Amount: "))

    # Append new expense to file
    with open("expenses.txt", "a") as file:

        file.write(f"{category},{amount}\n")

    print("New expense category added successfully.")


# Function to update an existing expense amount
def update_expense_amount():

    print("\n6. Update Existing Expense Amount")

    category = input("Enter Category To Update: ")

    new_amount = int(input("Enter New Amount: "))

    updated = False

    # Read all file data
    with open("expenses.txt", "r") as file:
        lines = file.readlines()

    # Rewrite file with updated data
    with open("expenses.txt", "w") as file:

        for line in lines:

            if line.strip():

                current_category, amount = line.strip().split(",")

                if current_category.lower() == category.lower():

                    file.write(f"{current_category},{new_amount}\n")

                    updated = True

                else:
                    file.write(line)

    if updated:
        print("Expense updated successfully.")
    else:
        print("Category not found.")


# Function to generate report.txt file
def generate_summary_report():

    total = calculate_total_expenditure()

    highest_spending, lowest_spending = find_highest_lowest_spending()

    with open("report.txt", "w") as report_file:

        report_file.write("---------- Expense Summary Report ----------\n\n")

        report_file.write(f"Total Expenses: Rs.{total}\n")

        report_file.write(
            f"Highest Expense Category: {highest_spending[0]} - Rs.{highest_spending[1]}\n"
        )

        report_file.write(
            f"Lowest Expense Category: {lowest_spending[0]} - Rs.{lowest_spending[1]}\n\n"
        )

        report_file.write("Categories Spending More Than Rs.800:\n")

        with open("expenses.txt", "r") as expenses_file:

            for line in expenses_file:

                if line.strip():

                    category, amount = line.strip().split(",")

                    amount = int(amount)

                    if amount > 800:
                        report_file.write(f"{category}: Rs.{amount}\n")

    print("\n7. Summary Report Generated Successfully.")
    print("Report saved in report.txt")


# ---------------- Calling Functions Sequentially ----------------

# 1. Display all expenses
display_expenses()

# 2. Calculate total expenditure
print("\n2. Total Expenditure")
total = calculate_total_expenditure()
print(f"Total Expenses = Rs.{total}")

# 3. Highest and Lowest Spending
print("\n3. Highest and Lowest Spending")

highest, lowest = find_highest_lowest_spending()

print(f"Highest Spending Category = {highest[0]} : Rs.{highest[1]}")
print(f"Lowest Spending Category = {lowest[0]} : Rs.{lowest[1]}")

# 4. Display expenses greater than ₹800
display_expenses_greater_than_800()

# 5. Add a new expense category
add_expense_category()

# 6. Update an existing expense amount
update_expense_amount()

# 7. Generate summary report
generate_summary_report()