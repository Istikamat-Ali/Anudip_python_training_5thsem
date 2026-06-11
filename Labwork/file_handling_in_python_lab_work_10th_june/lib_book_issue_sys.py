'''Constraints
• Use functions to modularize the program. 
• Use file handling (open(), read(), write(), append()). 
• Use lists/dictionaries wherever appropriate. 
• Do not use databases or external libraries. 
• Implement menu-driven execution using a while loop. 
• Ensure that updates are reflected in the original file
2. Library Book Issue System
Problem Statement
A library stores book information in books.txt.
File Format
B101,Python Basics,5
B102,Java Programming,2
B103,Data Science,0
B104,DBMS,3
B105,Machine Learning,1
B106,Operating Systems,4
B107,Networking,2
B108,Cyber Security,6
B109,Cloud Computing,0
B110,Web Development,3
Requirements
Develop a program to:
1. Display all books. 
2. Search a book using Book ID. 
3. Issue a book (decrease quantity by 1). 
4. Return a book (increase quantity by 1). 
5. Display unavailable books. 
6. Display books requiring restocking (copies < 2). 
7. Update the file after every issue/return operation.'''
print("------- Library Book Issue System -------")
#function to perform all operations
def display_all_books():
    with open("books.txt", "r") as file:
        for line in file:
            print(line.strip())
#search a book using book id
def search_book(book_id):
    with open("books.txt", "r") as file:
        for line in file:
            if line.startswith(book_id):
                return line #returning the line if book id is found
    return None
#issue a book (decrease quantity by 1)
def issue_book(book_id):
    with open("books.txt", "r") as file:
        lines = file.readlines() # it give the lines of the file in a list
    with open("books.txt", "w") as file:
        for line in lines: # reading line by line
            if line.startswith(book_id):
                quantity = int(line.split(",")[2]) #splitting line by comma
                if quantity > 0:
                    quantity -= 1
                    line = book_id, line.split(",")[1], str(quantity) + "\n" # assigning book id, title and quantity to line
            file.write(str(line)) # writing line to file
#return a book (increase quantity by 1)
def return_book(book_id):
    with open("books.txt", "r") as file:
        lines = file.readlines() # it give the lines of the file in a list
    with open("books.txt", "w") as file:
        for line in lines:
            if line.startswith(book_id):
                quantity = int(line.split(",")[2])
                quantity += 1
                line = book_id, line.split(",")[1], str(quantity) + "\n"
            file.write(str(line))
#display unavailable books
def display_unavailable_books():
    with open("books.txt", "r") as file:
        for line in file:
            quantity = int(line.split(",")[2])
            if quantity == 0:
                print(line.strip()) # strip is used to remove new line character
#display books requiring restocking (copies < 2)
def display_books_requiring_restocking():
    with open("books.txt", "r") as file:
        for line in file:
            quantity = int(line.split(",")[2])
            if quantity < 2:
                print(line.strip())
#update the file after every issue/return operation
def update_file():
    with open("books.txt", "r") as file:
        lines = file.readlines()
    with open("books.txt", "w") as file:
        for line in lines:
            file.write(line)
#calling functions
print("Display All Books:")
display_all_books()
print("Search a Book:")
print(search_book(input("Enter Book ID to Search: ")))
print("Issue a Book:")
issue_book(input("Enter Book ID to Issue: "))
print("Return a Book:")
return_book(input("Enter Book ID to Return: "))
print("Display Unavailable Books:")
display_unavailable_books()
print("Display Books Requiring Restocking:")
display_books_requiring_restocking()
print("Update File:")
update_file()
