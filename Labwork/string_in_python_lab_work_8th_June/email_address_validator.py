'''6. Email Address Validator
Problem Statement
A user enters an email address:
rahul.sharma2026@gmail.com
Tasks
Write a program to:
1. Extract username. 
2. Extract domain name. 
3. Extract extension. 
4. Count digits present in username. 
5. Count special characters. 
6. Check whether: 
o Exactly one '@' exists. 
o At least one '.' exists after '@'. 
7. Display Valid Email or Invalid Email. 
Sample Output
Email: rahul.sharma2026@gmail.com
Username: rahul.sharma2026
Domain: gmail
Extension: com
Digits Found: 4
Special Characters Found: 2
Email Status: Valid'''
print("---------------------Email Address Validator---------------------")
#email address from user is entered
email_address = "rahul.sharma2026@gmail.com"
print("email address:", email_address)
print("-------------------------------------------------------------")
#extract username
username = email_address.split("@")[0]#split("@") method is used to split the string into two parts based on "@"
print("Username:", username)
print("-------------------------------------------------------------")
#extract domain name
domain_name = email_address.split("@")[1].split(".")[0]#split("@")[1].split(".")[0] method is used to extract domain name based on "." and "@"
print("Domain:", domain_name)
print("-------------------------------------------------------------")
#extract extension
extension = email_address.split("@")[1].split(".")[1]
print("Extension:", extension)
print("-------------------------------------------------------------")
#count digits present in username
digits = 0
for char in username:
    if char.isdigit():
        digits += 1
print("Digits Found:", digits)
print("-------------------------------------------------------------")
#count special characters in emails uniquely
special_characters = 0
for char in email_address:
    if char in "!@#$%^&*()_+-=.":
        special_characters += 1
print("Special Characters Found:", special_characters)
print("-------------------------------------------------------------")
#check whether exactly one '@' exists
if "@" in email_address:
    if "." in email_address.split("@")[1]:
        print("Email Status: Valid")
    else:
        print("Email Status: Invalid")
else:
    print("Email Status: Invalid")
print("-------------------------------------------------------------")

