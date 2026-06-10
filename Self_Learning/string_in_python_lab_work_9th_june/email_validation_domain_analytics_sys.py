'''Assignment 2: Email Validation & Domain Analytics System 
Problem Statement 
An organization has collected 20 email addresses from users. 
Create a program to analyze these email addresses. 
Requirements 
For each email: 
1. Extract username.  
2. Extract domain.  
3. Extract extension.  
4. Count digits in username.  
5. Count special characters.  
6. Check if email is valid:  
o Exactly one '@'  
o Contains '.'  
o No spaces  
7. Display invalid emails.  
8. Count emails belonging to each domain.  
Sample Input 
rahul123@gmail.com 
priya@outlook.com 
anuj@company.in 
Challenge 
Generate a domain report: 
gmail.com     -> 8 users 
outlook.com   -> 5 users 
yahoo.com     -> 3 users 
company.in    -> 4 users '''
print("--------------------------Email Validation & Domain Analytics System--------------------------")
#creating empty list to store emails
email=[]
#taking input for emails
while len(email)<20:
    email.append(input("Enter email : ").strip())
print("---------------------------------------------------------------------------------")
#extracting username
for i in email:
    username=i.split("@")[0]
    print("Username:",username)
print("---------------------------------------------------------------------------------")
#extracting domain
for i in email:
    domain=i.split("@")[1]
    print("Domain:",domain)
print("---------------------------------------------------------------------------------")
#extracting extension
for i in email:
    extension=i.split("@")[1].split(".")[1]
    print("Extension:",extension)
print("---------------------------------------------------------------------------------")
#counting digits in username
for i in email:
    digits=0
    for j in i.split("@")[0]:
        if j.isdigit():
            digits+=1
    print("Digits in username:",digits)
print("---------------------------------------------------------------------------------")
#counting special characters
for i in email:
    special_characters=0
    for j in i.split("@")[0]:
        if j in "!@#$%^&*()_+-=":
            special_characters+=1
    print("Special characters in username:",special_characters)
print("---------------------------------------------------------------------------------")
#checking if email is valid
for i in email:
    if "@" in i and "." in i and " " not in i:
        print("Email is valid")
    else:
        print("Email is invalid")
print("---------------------------------------------------------------------------------")
#displaying invalid emails
for i in email:
    if "@" not in i or "." not in i or " " in i:
        print(i)
print("---------------------------------------------------------------------------------")
#counting emails belonging to each domain
domain_count={}
for i in email:
    domain=i.split("@")[1]
    if domain in domain_count:
        domain_count[domain]+=1
    else:
        domain_count[domain]=1
for i in domain_count:
    print(i,"->",domain_count[i])
print("---------------------------------------------------------------------------------")
print("Challenge")
#generating domain report
for i in domain_count:
    print(i,"->",domain_count[i])
print("---------------------------------------------------------------------------------")
