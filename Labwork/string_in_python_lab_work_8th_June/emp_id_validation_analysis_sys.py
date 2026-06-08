'''1. Employee ID Validation and Analysis System
Problem Statement
A company generates employee IDs in the following format:
EMP2026ANUJ458
Tasks
Write a program to:
1. Count the number of uppercase letters. 
2. Count the number of digits. 
3. Extract the joining year. 
4. Extract the employee name. 
5. Check whether the ID follows these rules: 
o Starts with "EMP" 
o Contains exactly 4 digits for the year 
o Ends with exactly 3 digits 
6. Create a list containing all digits present in the ID. 
7. Find the sum of all digits present in the ID. 
8. Display whether the ID is valid or invalid. 
Sample Output
Employee ID: EMP2026ANUJ458
Uppercase Letters: 7
Digits: 7
Joining Year: 2026
Employee Name: ANUJ
Digit List: [2, 0, 2, 6, 4, 5, 8]
Sum of Digits: 27
ID Status: Valid'''
print("---------------------Employee ID Validation and Analysis System---------------------")
# input employee ID from user
employee_id = input("Enter Employee ID: ")
# validating the input
if employee_id.startswith("EMP"):
    pass
else:
    exit("Employee ID should start with 'EMP' ...Exited")
print("---------------------------------------------------------------------------------")
# counting the number of uppercase letters
uppercase_letters = sum(1 for char in employee_id if char.isupper())#this is a list comprehension for counting uppercase letters
print("Uppercase Letters:", uppercase_letters)
print("---------------------------------------------------------------------------------")
# counting the number of digits
digits = sum(1 for char in employee_id if char.isdigit())#this is a list comprehension for counting digits
print("Digits:", digits)
print("---------------------------------------------------------------------------------")
# extracting the joining year
joining_year = employee_id[3:7]
print("Joining Year:", joining_year)
print("---------------------------------------------------------------------------------")
# extracting the employee name
employee_name = employee_id[7:-3]
print("Employee Name:", employee_name)
print("---------------------------------------------------------------------------------")
# creating a list containing all digits present in the ID
digit_list = [int(char) for char in employee_id if char.isdigit()]
print("Digit List:", digit_list)
print("---------------------------------------------------------------------------------")
# finding the sum of all digits present in the ID
sum_of_digits = sum(digit_list)
print("Sum of Digits:", sum_of_digits)
print("---------------------------------------------------------------------------------")
# displaying whether the ID is valid or invalid
# Reconstruct the expected ID to validate it
reconstructed_id = "EMP" + joining_year + employee_name + "".join(str(d) for d in digit_list[4:])#join method is used to convert list to string
# Check validity
total_digits_at_end = sum(1 for char in employee_id[-3:] if char.isdigit())#this is a list comprehension for counting digits
if employee_id == reconstructed_id and total_digits_at_end > 0:# total digits at end should be greater than 0
    id_status = "Valid"
else:
    id_status = "Invalid"
print("ID Status:", id_status)
print("---------------------------------------------------------------------------------")

