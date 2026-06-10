'''Assignment 1: Password Security Analyzer 
Problem Statement 
A cybersecurity company wants to analyze user passwords before allowing account creation. 
The system should accept at least 15 passwords and generate a security report. 
Requirements 
For each password: 
1. Count uppercase letters.  
2. Count lowercase letters.  
3. Count digits.  
4. Count special characters.  
5. Check minimum length (8 characters).  
6. Check if spaces exist.  
7. Determine password strength:  
o Strong  
o Medium  
o Weak  
8. Display repeated characters.  
9. Count vowels and consonants.  
10. Identify the most frequently occurring character.  
Challenge 
Generate a report showing: 
Total Passwords Analyzed 
Strong Passwords 
Medium Passwords 
Weak Passwords '''
print("--------------------------Password Security Analyzer--------------------------")
#creating empty list  to store password entered by user
password=[]
#taking input for passwords
while len(password)<15:
    password.append(input("Enter the password : "))
#counting uppercase letters
print("---------------------------------------------------------------------------------")
print("Count uppercase letters:")
for i in password:
    count=0
    for j in i:
        if j.isupper():
            count+=1
    print(i,"->",count)
print("---------------------------------------------------------------------------------")
#counting lowercase letters
print("Count lowercase letters:")
for i in password:#for each password in password
    count=0
    for j in i:#for each character in a password
        if j.islower():
            count+=1
    print(i, "->",count)
print("---------------------------------------------------------------------------------")
#counting digits
print("Count digits:")
for i in password:
    count=0
    for j in i:
        if j.isdigit():#checking if the character is a digit in each password
            count+=1
    print(i,"->",count)  
print("---------------------------------------------------------------------------------")
#counting special characters
print("Count special characters:")
for i in password:
    count=0
    for j in i:
        if j in "!@#$%^&*()_+-=":
            count+=1
    print(i,"->",count)
print("---------------------------------------------------------------------------------")
#checking minimum length
print("Checking minimum length:")
for i in password:
    if len(i)>=8:
        print(i,"has characters more than 8")#if the length of the password is greater than or equal to 8, it is a strong password
    else:
        print(i,"has characters less than 8")
print("---------------------------------------------------------------------------------")
#checking for spaces
print("Checking for spaces:")
for i in password:
    if " " in i:
        print(i,"has spaces")
    else:
        print(i,"has no spaces")
print("---------------------------------------------------------------------------------")
#determine password strength
for i in password:
    uppercase_letters=0
    lowercase_letters=0
    digits=0
    special_characters=0
    for j in i:
        if j.isupper():
            uppercase_letters+=1
        elif j.islower():
            lowercase_letters+=1
        elif j.isdigit():
            digits+=1
        elif j in "!@#$%^&*()_+-=":
            special_characters+=1
    if uppercase_letters>=1 and lowercase_letters>=1 and digits>=1 and special_characters>=1:
        print(i,"is a strong password")
    elif uppercase_letters>=1 and lowercase_letters>=1 and digits>=1:
        print(i,"is a medium password")
    else:
        print(i,"is a weak password")
print("---------------------------------------------------------------------------------")
#displaying repeated characters
print("Displaying repeated characters:")
frequency={}  
for i in password:
    freq={}
    for j in i:
        if j in freq:
            freq[j]+=1
        else:
            freq[j]=1
    frequency[i]=freq
#printing passwords with repeated characters
for i in frequency:
    for j in frequency[i]:
        if frequency[i][j]>1:
            print(i,"->",j,"->",frequency[i][j])
print("---------------------------------------------------------------------------------")
#printing characters and their frequencies in each password
for i in frequency:
    print(i,frequency[i])
print("---------------------------------------------------------------------------------")
#counting vowels and consonants
print("Counting vowels and consonants:")
vowels=0
consonants=0
for i in password:
    for j in i:
        if j.isalpha():
            if j in "aeiouAEIOU":
                vowels+=1
            else:
                consonants+=1
    print(i,"has",vowels,"vowels","and",consonants,"consonants")#print the number of vowels and consonants in each passwordconsonants)
print("---------------------------------------------------------------------------------")
#identifying the most frequently occurring character
print("Identifying the most frequently occurring character:")
for i in password:
    freq={}
    for j in i:
        if j in freq:
            freq[j]+=1
        else:
            freq[j]=1
    for val in freq.values():
        if val==max(freq.values()):
            for key in freq.keys():
                if freq[key]==val:
                    print("The most frequently occurring character in",i,"is",key,val)
            break
    































