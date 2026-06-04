# Palindrome and Reverse Number Checker
# Problem Statement:
# Accept a number from the user.
# Display:
# • Reverse Number 
# • Whether it is a Palindrome 
# Example:
# Input: 1221
# Output:
# Reverse: 1221
# Palindrome Number
#program to check if a number is a palindrome and to reverse the number
# input a number from user
number = int(input("Enter a number: "))
# validating the input
if number < 0:
    exit("Negative numbers cannot be considered for palindromes ...Exited")
print("-------------------------------------------------------------")
# storing original number
original_number = number #for later comparison, as we will be modifying the number variable to calculate reverse and check palindrome condition
# initializing variable for reverse number
reverse_number = 0
# calculating reverse number
while number > 0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number = number // 10
# displaying the reverse number
print("Reverse:", reverse_number)
# checking palindrome condition
if original_number == reverse_number:
    print(original_number, "is a Palindrome number.")
else:
    print(original_number, "is not a Palindrome number.")