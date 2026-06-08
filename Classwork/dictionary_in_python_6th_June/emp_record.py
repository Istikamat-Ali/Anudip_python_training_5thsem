'''Write a program to create a dictionary that contains the record of 10 employs where emp id is used as a key and salary as value 
find out the total no of emp having salary greater than 30000 
find out the total no of emp having salary below  the 20000'''
#taking input for 10 employees
employees = {}
for i in range(10):
    emp_id = int(input("Enter employee id: "))
    salary = int(input("Enter employee salary: "))
    employees[emp_id] = salary
#find out the total no of emp having salary greater than 30000
count = 0
for emp_id, salary in employees.items():#emp_id is key and salary is value and employees.item () gives key and value
    if salary > 30000:
        count += 1
print("Total employees with salary greater than 30000:", count)
#find out the total no of emp having salary below  the 20000
count = 0
for emp_id, salary in employees.items():
    if salary < 20000:
        count += 1
print("Total employees with salary below 20000:", count)