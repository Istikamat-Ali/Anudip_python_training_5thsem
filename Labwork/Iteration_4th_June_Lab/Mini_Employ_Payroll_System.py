# Problem Statement:
# Accept:
# • Employee Name 
# • Basic Salary 
# Calculate:
# Component Percentage
# HRA 20%
# DA 10%
# PF Deduction 12%
# Display:
# • Gross Salary 
# • Net Salary 
# Additionally:
# Net Salary > 50000 → Senior Grade
# Net Salary > 30000 → Mid Grade
#Else → Junior Grade
#program to manage employee payroll system
print("---------------------Mini Employee Payroll System---------------------")
# input employee name and basic salary from user
employee_name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: ₹"))
# validating the input
if basic_salary < 0:
    exit("Basic Salary cannot be negative ...Exited")
print("-------------------------------------------------------------")
# calculating components based on percentage
hra = basic_salary * 0.20  # HRA is 20% of basic salary
da = basic_salary * 0.10   # DA is 10% of basic salary
pf_deduction = basic_salary * 0.12  # PF deduction is 12% of basic salary
# calculating gross salary and net salary
gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf_deduction
# determining grade based on net salary
if net_salary > 50000:
    grade = "Senior Grade"  
elif net_salary > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"
# displaying the result
print("Employee Name:", employee_name)
print("Basic Salary: ₹", basic_salary)
print("HRA: ₹", hra)
print("DA: ₹", da)
print("PF Deduction: ₹", pf_deduction)
print("Gross Salary: ₹", gross_salary)
print("Net Salary: ₹", net_salary)
print("Grade:", grade)      