'''Constraints
• Use functions to modularize the program. 
• Use file handling (open(), read(), write(), append()). 
• Use lists/dictionaries wherever appropriate. 
• Do not use databases or external libraries. 
• Implement menu-driven execution using a while loop. 
• Ensure that updates are reflected in the original file.
1. Employee Payroll Management System
Problem Statement
A company stores employee details in a text file named employees.txt.
File Format
EMP101,Anuj,45000
EMP102,Rahul,52000
EMP103,Priya,38000
EMP104,Neha,61000
EMP105,Amit,29000
EMP106,Sneha,55000
EMP107,Karan,47000
EMP108,Pooja,72000
EMP109,Rohit,33000
EMP110,Anjali,68000
Requirements
Create a menu-driven program to:
1. Display all employee records. 
2. Search employee details using Employee ID. 
3. Calculate the average salary. 
4. Find the highest-paid and lowest-paid employee. 
5. Display employees earning above ₹50,000. 
6. Add a new employee record to the file. 
7. Generate salary categories: 
o High (₹60,000 and above) 
o Medium (₹40,000–₹59,999) 
o Low (Below ₹40,000)'''
print("---------------------Employee Payroll Management System---------------------")
# Function to display all employee records
def display_all_employees():
    with open("employees.txt", "r") as file:
        for line in file:#reading line by line
            print(line.strip())#removing new line character
# Function to search employee details using Employee ID
def search_employee(employee_id):
    with open("employees.txt", "r") as file:
        content=file.read()
        for line in content.split("\n"):
            if line.startswith(employee_id):
                return line
    return None
# Function to calculate the average salary
def calculate_average_salary():
    total_salary = 0
    employee_count = 0
    with open("employees.txt", "r") as file:
        for line in file:#reading line by line
            employee_id, _, salary = line.strip().split(",")#splitting line by comma
            total_salary += int(salary)#converting string to integer
            employee_count += 1
    if employee_count > 0:
        return total_salary / employee_count #average salary is total salary divided by employee count
    return 0#returning 0 if employee count is 0
# Function to find the highest-paid and lowest-paid employee
def find_highest_lowest_paid():
    highest_paid = None # variable to store highest paid employee and its salary as tuple and None is used to initialize because it will be assigned a value later
    lowest_paid = None #None is assigned to lowest paid employee and its salary as tuple 
    with open("employees.txt", "r") as file:
        for line in file:#reading line by line
            employee_id, _, salary = line.strip().split(",")#splitting line by comma
            salary = int(salary)
            if highest_paid is None or salary > highest_paid[1]:#if highest paid employee is None or salary of employee is greater than highest paid employee
                highest_paid = (employee_id, salary) #assigning employee id and salary to highest paid employee
            if lowest_paid is None or salary < lowest_paid[1]: #if lowest paid employee is None or salary of employee is less than lowest paid employee
                lowest_paid = (employee_id, salary) #assigning employee id and salary to lowest paid employee
    return highest_paid, lowest_paid
# Function to display employees earning above ₹50,000
def display_employees_above_50000():
    with open("employees.txt", "r") as file:
        for line in file:#reading line by line
            employee_id, _, salary = line.strip().split(",")#splitting line by comma
            salary = int(salary)
            if salary > 50000:
                print(employee_id, salary)
# Function to add a new employee record to the file
def add_employee(employee_id, name, salary):
    with open("employees.txt", "a") as file:# appending to file 
        file.write(f"{employee_id},{name},{salary}\n") # writing employee id, name and salary to file
# Function to generate salary categories
def generate_salary_categories():
    with open("employees.txt", "r") as file:
        for line in file:#reading line by line
            employee_id, _, salary = line.strip().split(",")#splitting line by comma
            salary = int(salary)
            if salary >= 60000:
                print(f"{employee_id} is in High Salary category.")
            elif 40000 <= salary < 60000:
                print(f"{employee_id} is in Medium Salary category.")
            else:
                print(f"{employee_id} is in Low Salary category.")
# Main menu
while True:
    print("\nEmployee Payroll Management System")
    print("1. Display all employee records")
    print("2. Search employee details using Employee ID")
    print("3. Calculate the average salary")
    print("4. Find the highest-paid and lowest-paid employee")
    print("5. Display employees earning above ₹50,000")
    print("6. Add a new employee record to the file")
    print("7. Generate salary categories")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")
    if choice == "1":
        display_all_employees()
    elif choice == "2":
        employee_id = input("Enter Employee ID: ")
        employee_details = search_employee(employee_id)
        if employee_details:
            print(employee_details)
        else:
            print("Employee not found.")
    elif choice == "3":
        average_salary = calculate_average_salary()
        print("Average Salary:", average_salary)
    elif choice == "4":
        highest_paid, lowest_paid = find_highest_lowest_paid()
        print("Highest-Paid Employee:", highest_paid)
        print("Lowest-Paid Employee:", lowest_paid)
    elif choice == "5":
        display_employees_above_50000()
    elif choice == "6":
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = input("Enter Employee Salary: ")
        add_employee(employee_id, name, salary)
        print("Employee record added successfully.")
    elif choice == "7":
        generate_salary_categories()
    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")

