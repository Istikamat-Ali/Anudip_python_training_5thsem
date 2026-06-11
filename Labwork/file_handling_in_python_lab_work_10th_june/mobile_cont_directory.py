'''Constraints
• Use functions to modularize the program. 
• Use file handling (open(), read(), write(), append()). 
• Use lists/dictionaries wherever appropriate. 
• Do not use databases or external libraries. 
• Implement menu-driven execution using a while loop. 
• Ensure that updates are reflected in the original file
4. Mobile Contact Directory System
Problem Statement
Contacts are stored in contacts.txt.
File Format
Anuj,9876543210
Rahul,9876543211
Priya,9876543212
Neha,9876543213
Amit,9876543214
Sneha,9876543215
Karan,9876543216
Pooja,9876543217
Rohit,9876543218
Anjali,9876543219
Requirements
Create a menu-driven application to:
1. Display all contacts. 
2. Search a contact by name. 
3. Add a new contact. 
4. Update an existing contact number. 
5. Delete a contact. 
6. Display contacts whose names start with a vowel. 
7. Save all modifications back to the file.'''
# function to display all contacts
def display_contacts():
    with open("contacts.txt", "r") as file:
        contacts = file.readlines() # it give the lines of the file in a list
        for contact in contacts:# for reading line by line
            name, phone = contact.strip().split(",") # splitting line by comma and assigning name and phone to variables
            print(f"Name: {name}, Phone: {phone}")
# function to search a contact by name
def search_contact(name):
    with open("contacts.txt", "r") as file:
        contacts = file.readlines() # it give the lines of the file in a list
        for contact in contacts:
            contact_name, _ = contact.strip().split(",") # splitting line by comma and assigning name and phone to variables
            if contact_name == name:
                return contact
        return None
# function to add a new contact
def add_contact(name, phone):
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone}\n")
# function to update a contact number
def update_contact(name, phone):
    with open("contacts.txt", "r") as file:
        contacts = file.readlines() # it give the lines of the file in a list
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            contact_name, _ = contact.strip().split(",") # splitting line by comma and assigning name and phone to variables
            if contact_name == name:# if contact name is equal to name
                file.write(f"{name},{phone}\n")# updating contact
            else:
                file.write(contact)# writing contact to file if contact name is not equal to name
# function to delete a contact
def delete_contact(name):
    with open("contacts.txt", "r") as file:
        contacts = file.readlines() # it give the lines of the file in a list
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            contact_name, _ = contact.strip().split(",") # splitting line by comma and assigning name and phone to variables
            if contact_name != name:# if contact name is not equal to name
                file.write(contact)# writing contact to file whose name is not equal to name
            else:
                print(f"Contact {name} deleted successfully.") #name of contact to be deleted as name matched so not written into file 
# function to display contacts whose names start with a vowel
def display_vowel_contacts():
    with open("contacts.txt", "r") as file:
        contacts = file.readlines() # it give the lines of the file in a list
        for contact in contacts:
            name, _ = contact.strip().split(",") # splitting line by comma and assigning name and phone to variables
            if name[0].lower() in "aeiou":# if name starts with a vowel
                print(contact.strip())# printing contact
# function to save all modifications back to the file
def save_modifications():
    with open("contacts.txt", "r") as file:
        contacts = file.readlines() # it give the lines of the file in a list
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(contact)
print("--------------Mobile Contact Directory System--------------")
while True:
    print("1. Display all contacts")
    print("2. Search a contact by name")
    print("3. Add a new contact")
    print("4. Update an existing contact number")
    print("5. Delete a contact")
    print("6. Display contacts whose names start with a vowel")
    print("7. Save all modifications back to the file")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        display_contacts()
    elif choice == "2":
        name = input("Enter the name to search: ")
        contact = search_contact(name)
        if contact:
            print(contact)
        else:
            print("Contact not found.")
    elif choice == "3":
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        add_contact(name, phone)
        print("Contact added successfully.")
    elif choice == "4":
        name = input("Enter the name to update: ")
        phone = input("Enter the new phone number: ")
        update_contact(name, phone)
        print("Contact updated successfully.")
    elif choice == "5":
        name = input("Enter the name to delete: ")
        delete_contact(name)
    elif choice == "6":
        display_vowel_contacts()
    elif choice == "7":
        save_modifications()
        print("All modifications saved successfully.")
    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")

