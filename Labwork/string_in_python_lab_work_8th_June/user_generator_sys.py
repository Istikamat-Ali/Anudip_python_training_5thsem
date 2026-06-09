'''7. Username Generator System
Problem Statement
A student enters:
Rahul Sharma
Tasks
Generate a username using the rules:
1. Remove spaces. 
2. Convert to lowercase. 
3. Append current year (2026). 
4. If username length exceeds 12, keep only first 12 characters. 
5. Count vowels in the generated username. 
6. Count consonants. 
7. Display username statistics. 
Sample Output
Original Name: Rahul Sharma
Generated Username:
rahulsharma2026
Username Length: 15
Vowels: 5
Consonants: 10
Status: Username Generated Successfully'''
print("---------------------Username Generator System---------------------")
#user enters name
name = "Rahul Sharma"
print("Original Name:", name)
print("-------------------------------------------------------------")
#remove spaces
username = name.replace(" ", "")
print("Generated Username:", username)
print("-------------------------------------------------------------")
#convert to lowercase
username = username.lower()
print("Generated Username:", username)
print("-------------------------------------------------------------")
#append current year
username += "2026"
print("Username Length:", len(username))
print("-------------------------------------------------------------")
#count vowels and consonants
vowels = sum(1 for char in username if char in "aeiouAEIOU")
consonants = sum(1 for char in username if char not in "aeiouAEIOU")
print("Vowels:", vowels)
print("Consonants:", consonants)
print("-------------------------------------------------------------")
#display username statistics
print("Status: Username Generated Successfully")
print("-------------------------------------------------------------")
