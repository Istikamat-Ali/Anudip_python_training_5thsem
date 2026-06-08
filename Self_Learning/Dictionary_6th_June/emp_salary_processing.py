'''3. Employee Salary Processing
Sample Data
employee_salary = {
 "EMP101": 45000,
 "EMP102": 62000,
 "EMP103": 38000,
 "EMP104": 75000,
 "EMP105": 54000,
 "EMP106": 29000,
 "EMP107": 82000,
 "EMP108": 48000,
 "EMP109": 36000,
 "EMP110": 68000
}
Tasks
• Display employees earning above ₹60,000. 
• Count employees earning below ₹40,000. 
• Find the highest-paid employee. 
• Create a list of employees eligible for a bonus (salary > ₹50,000). 
• Calculate the average salary'''
print("---------------------Employee Salary Processing---------------------")
# Dictionary of employees and their salaries
employee_salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}
# Task 1: Display employees earning above ₹60,000
print("Employees Earning above ₹60,000:")
for employee, salary in employee_salary.items():
    if salary > 60000:
        print(employee, salary)
print("---------------------------------")
# Task 2: Count employees earning below ₹40,000
count = sum(1 for _, salary in employee_salary.items() if salary < 40000)
print("Employees Earning below ₹40,000:", count)
print("---------------------------------")
# Task 3: Find the highest-paid employee
highest_paid = max(employee_salary, key=employee_salary.get)
print("Highest-paid employee:", highest_paid, employee_salary[highest_paid])
print("---------------------------------")
# Task 4: Create a list of employees eligible for a bonus
bonus_eligible = [employee for employee, salary in employee_salary.items() if salary > 50000]
print("Employees eligible for a bonus:", bonus_eligible)
print("---------------------------------")
# Task 5: Calculate the average salary
total_salary = sum(employee_salary.values())
average_salary = total_salary / len(employee_salary)
print("Average salary:", average_salary)
print("---------------------------------")

