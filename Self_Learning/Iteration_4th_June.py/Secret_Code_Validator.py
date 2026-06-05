# 5.> program to validate a secret code
print("---------------------Secret Code Validator---------------------")
# input a secret code from user
secret_code = input("Enter a secret code: ")
# validating the input
if len(secret_code) !=6 or not secret_code.isdigit():# checking if the secret code is a 6-digit number and isdigit() method checks if all characters in the string are digits
    exit("Secret code should be a 6-digit number...Exited")
print("-------------------------------------------------------------")
# calculating sum of first 3 digits and last 3 digits using for loop
sum_first_half = 0
sum_second_half = 0
for i in range(3):
    sum_first_half += int(secret_code[i]) # adding the integer value of the current digit to sum_first_half
    sum_second_half += int(secret_code[i+3]) # adding the integer value of the current digit to sum_second_half
# validating the secret code by comparing the sums of the two halves
if sum_first_half == sum_second_half:
    print("Valid Code")
else:    
    print("Invalid Code")