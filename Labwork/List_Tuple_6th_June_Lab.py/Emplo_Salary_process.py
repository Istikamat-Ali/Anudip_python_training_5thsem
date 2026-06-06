'''4. Employee Salary Processing
Problem Statement
Employee data is stored as tuples:
employees = [
 ("Rahul", 35000),
 ("Priya", 55000),
 ("Amit", 42000),
 ("Neha", 65000)
]
Write a program to:
• Display employees earning above ₹50,000. 
• Find the highest-paid employee. 
• Calculate total salary expenditure. 
• Count employees earning below ₹40,000.
'''
print("---------------------Employee Salary Processing---------------------")
# List of employees and their salaries
employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]
# Task 1: Display employees earning above ₹50,000
print("Employees Earning above ₹50,000:")
for employee, salary in employees:
    if salary > 50000:
        print(employee, salary)
print("---------------------------------")
#-----------------------------------------
# Task 2: Find the highest-paid employee
highest_paid=employees[0]
for employee, salary in employees:
    if salary > highest_paid[1]:
        highest_paid = (employee, salary)
print("Highest-Paid Employee:", highest_paid[0])
print("---------------------------------")
#-----------------------------------------
# Task 3: Calculate total salary expenditure    
total_expenditure = 0
for _,salary in employee:
    total_expenditure += salary 
print("Total Salary Expenditure:", total_expenditure)
print("---------------------------------")
#-----------------------------------------
# Task 4: Count employees earning below ₹40,000
count = sum(1 for _, salary in employees if salary < 40000) #this method is called as generator.
print("Employees Earning below ₹40,000:", count)
print("---------------------------------")
