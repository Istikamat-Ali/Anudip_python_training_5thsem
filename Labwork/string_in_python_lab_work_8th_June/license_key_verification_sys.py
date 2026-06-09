'''9. License Key Verification System
Problem Statement
A software license key is entered:
ABCD-EFGH-IJKL-MNOP
Tasks
Write a program to:
1. Verify there are exactly 4 groups. 
2. Verify each group contains exactly 4 characters. 
3. Count total letters. 
4. Count vowels. 
5. Remove hyphens and display the merged key. 
6. Create a list containing all groups. 
7. Display whether the key format is valid. 
Sample Output
License Key:
ABCD-EFGH-IJKL-MNOP
Groups:
['ABCD', 'EFGH', 'IJKL', 'MNOP']
Number of Groups: 4
Total Letters: 16
Total Vowels: 4
Merged Key:
ABCDEFGHIJKLMNOP
License Key Status: Valid'''
print("---------------------License Key Verification System---------------------")
#license key from user is entered
license_key = "ABCD-EFGH-IJKL-MNOP"
print("-------------------------------------------------------------")
#verify there are exactly 4 groups
groups = license_key.split("-")
if len(groups) != 4:
    print("License Key Status: Invalid")
else:
    print("Groups:", groups)
    print("Number of Groups:", len(groups))
print("-------------------------------------------------------------")
#verify each group contains exactly 4 characters
for group in groups:
    if len(group) != 4:
        print("License Key Status: Invalid")
        break
else:
    print("License Key Status: Valid")
print("-------------------------------------------------------------")
#count total letters
total_letters = 0
for group in groups:#group is a string and groups are in the form of list
    total_letters += len(group)
print("Total Letters:", total_letters)
print("-------------------------------------------------------------")
#count vowels
vowels = 0
for group in groups:
    for char in group:
        if char in "aeiouAEIOU":
            vowels += 1
print("Total Vowels:", vowels)
print("-------------------------------------------------------------")
#remove hyphens and display the merged key
merged_key = "".join(groups)#join method is used to convert list to string and group is a list of strings separated by hyphens only strings
print("Merged Key:", merged_key)
print("-------------------------------------------------------------")
#display whether the key format is valid
print("License Key Status: Valid")
print("-------------------------------------------------------------")