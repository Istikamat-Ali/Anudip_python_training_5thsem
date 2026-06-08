'''9. Mobile Contact Directory
Sample Data
contacts = {
 "Amit": "9876543210",
 "Priya": "9876543211",
 "Rohan": "9876543212",
 "Neha": "9876543213",
 "Anjali": "9876543214",
 "Karan": "9876543215",
 "Pooja": "9876543216",
 "Arjun": "9876543217",
 "Sneha": "9876543218",
 "Rahul": "9876543219"
}
Tasks
• Display all contact names in alphabetical order. 
• Count the total number of contacts. 
• Search for a given contact name. 
• Create a list of contacts whose names start with a vowel. 
• Stop the search using break once the required contact is found'''
print("---------------------Mobile Contect Directory----------------------")
#Given dictionary for contact directory 
contacts = {
 "Amit": "9876543210",
 "Priya": "9876543211",
 "Rohan": "9876543212",
 "Neha": "9876543213",
 "Anjali": "9876543214",
 "Karan": "9876543215",
 "Pooja": "9876543216",
 "Arjun": "9876543217",
 "Sneha": "9876543218",
 "Rahul": "9876543219"
}
print("-------------------------------------------------------------------")
#Display all contact names in alphabetical order
print("All contact names in alphabetical order:")
for key in sorted(contacts.keys()):
    print(key)
print("-------------------------------------------------------------------")
#Count the total number of contacts
print("Total number of contacts:",len(contacts))
print("-------------------------------------------------------------------")
#Search for a given contact name
search_name=input("Enter the contact name to search:")
if search_name in contacts:
    print(search_name,"is present in the contact directory.")
else:
    print(search_name,"is not present in the contact directory.")
print("-------------------------------------------------------------------")
#Create a list of contacts whose names start with a vowel
vowel_contacts = [name for name in contacts if name[0] in "aeiouAEIOU"]
print("Contacts whose names start with a vowel:")
for name in vowel_contacts:
    print(name)
print("-------------------------------------------------------------------")
#Stop the search using break once the required contact is found
search_name=input("Enter the contact name to search:")
for name,contact in contacts.items():
    if name == search_name:
        print(search_name,"is present in the contact directory.")
        break
else:
    print(search_name,"is not present in the contact directory.")
print("-------------------------------------------------------------------")