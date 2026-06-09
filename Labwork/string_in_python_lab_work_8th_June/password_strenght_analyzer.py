'''2. Password Strength Analyzer
Problem Statement
A user enters a password.
Python@2026!
Tasks
Write a program to determine whether the password is Strong, Medium, or Weak.
Rules:
• Minimum length 8 
• Contains at least: 
o 1 uppercase letter 
o 1 lowercase letter 
o 1 digit 
o 1 special character 
Additionally:
1. Count uppercase letters. 
2. Count lowercase letters. 
3. Count digits. 
4. Count special characters. 
5. Display all digits separately. 
6. Display all special characters separately. 
Sample Output
Password: Python@2026!
Uppercase Letters: 1
Lowercase Letters: 5
Digits: 4
Special Characters: 2
Digits Found: ['2', '0', '2', '6']
Special Characters Found: ['@', '!']
Password Strength: Strong'''
print("---------------------Password Strength Analyzer---------------------")
# input password from user
password = input("Enter Password: ")
# determine whether the password is Strong, Medium, or Weak
#password length must be greater than or equal to 8
if len(password) < 8:
    exit("Password length must be at least 8 characters. Exited")
else:
    if any(char.isupper() for char in password):#this is a list comprehension for checking uppercase
        if any(char.islower() for char in password):
            if any(char.isdigit() for char in password):
                if any(char in "!@#$%^&*()_+-=" for char in password):
                    print("Strong")
                else:
                    print("Meduim")
            else:
                print("Medium")
        else:
            print("Weak")
    else:
        print("Weak")
print("---------------------------------------------------------------------------------")
# counting the number of uppercase letters
uppercase_letters = sum(1 for char in password if char.isupper())
print("Uppercase Letters:", uppercase_letters)
print("---------------------------------------------------------------------------------")
# counting the number of lowercase letters
lowercase_letters = sum(1 for char in password if char.islower())
print("Lowercase Letters:", lowercase_letters)        
print("---------------------------------------------------------------------------------")
# counting the number of digits
digits = sum(1 for char in password if char.isdigit())
print("Digits:", digits)
print("---------------------------------------------------------------------------------")
# counting the number of special characters
special_characters = sum(1 for char in password if char in "!@#$%^&*()_+-=")
print("Special Characters:", special_characters)
print("---------------------------------------------------------------------------------")
# displaying all digits separately
digits_found = [char for char in password if char.isdigit()]
print("Digits Found:", digits_found)
print("---------------------------------------------------------------------------------")
# displaying all special characters separately
special_characters_found = [char for char in password if char in "!@#$%^&*()_+-="]
print("Special Characters Found:", special_characters_found)
print("---------------------------------------------------------------------------------")
# determining the strength of the password
if uppercase_letters >= 1 and lowercase_letters >= 1 and digits >= 1 and special_characters >= 1:
    password_strength = "Strong"
elif uppercase_letters >= 1 and lowercase_letters >= 1 and digits >= 1:
    password_strength = "Medium"
else:
    password_strength = "Weak"
print("Password Strength:", password_strength)
print("---------------------------------------------------------------------------------")