print("--------------------- Employee ID Validation and Analysis System ---------------------")

# Input Employee ID
employee_id = input("Enter Employee ID: ").strip()

print("Employee ID:", employee_id)
print("---------------------------------------------------------------------------------")

# Count uppercase letters
uppercase_letters = sum(1 for char in employee_id if char.isupper())
print("Uppercase Letters:", uppercase_letters)

print("---------------------------------------------------------------------------------")

# Count digits
digit_count = sum(1 for char in employee_id if char.isdigit())
print("Digits:", digit_count)

print("---------------------------------------------------------------------------------")

# Extract joining year (characters from index 3 to 6)
joining_year = employee_id[3:7]
print("Joining Year:", joining_year)

print("---------------------------------------------------------------------------------")

# Extract employee name (between year and last 3 digits)
employee_name = employee_id[7:-3]
print("Employee Name:", employee_name)

print("---------------------------------------------------------------------------------")

# Create a list of all digits present in ID
digit_list = [int(char) for char in employee_id if char.isdigit()]
print("Digit List:", digit_list)

print("---------------------------------------------------------------------------------")

# Find sum of all digits
sum_of_digits = sum(digit_list)
print("Sum of Digits:", sum_of_digits)

print("---------------------------------------------------------------------------------")

# ---------------- VALIDATION ----------------

# Rule 1: ID must start with EMP
starts_with_emp = employee_id.startswith("EMP")

# Rule 2: Year must contain exactly 4 digits
valid_year = joining_year.isdigit() and len(joining_year) == 4

# Rule 3: Last 3 characters must be digits
valid_end_digits = employee_id[-3:].isdigit()

# Rule 4: Employee name should contain only uppercase letters
valid_name = employee_name.isalpha() and employee_name.isupper()

# Final Validation
if starts_with_emp and valid_year and valid_end_digits and valid_name:
    id_status = "Valid"
else:
    id_status = "Invalid"

print("ID Status:", id_status)

print("---------------------------------------------------------------------------------")