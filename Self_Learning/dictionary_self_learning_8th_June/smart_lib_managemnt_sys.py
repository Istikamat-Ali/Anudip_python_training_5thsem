'''3. Smart Library Management System
Problem Statement
Create a digital library management system.
Example Structure
library = {
 "B101": {
 "title": "Python Basics",
 "author": "ABC",
 "copies": 5
 }
}
Maintain records of at least 30 books.
Requirements
1. Add a book. 
2. Remove a book. 
3. Search a book by ID. 
4. Search by title. 
5. Update available copies. 
6. Issue a book. 
7. Return a book. 
8. Display books with fewer than 3 copies. 
9. Display books that are unavailable. 
10. Find the most available book. 
11. Generate a restocking report. 
12. Create a separate dictionary of books requiring immediate purchase. 
Challenge
Generate a complete library summary report.'''
print("------- Smart Library Management System -------")
# taking input from user in this format
'''library = {
    "B101": {
        "title": "Python Basics",
        "author": "ABC",
        "copies": 5
    }
}'''
library = {}
for i in range(10):
    book_id = input("Enter Book ID: ")
    book_title = input("Enter Book Title: ")
    book_author = input("Enter Book Author: ")
    book_copies = int(input("Enter Book Copies: "))
    library[book_id] = {
        "title": book_title,
        "author": book_author,
        "copies": book_copies
    }
print("---------------------------------------------------------------------------------")
#Task 1: Add a Book
# --------------------------------------------------
print("Add a Book:")
#add a book
book_id = input("Enter Book ID: ")
book_title = input("Enter Book Title: ")
book_author = input("Enter Book Author: ")
book_copies = int(input("Enter Book Copies: "))
library[book_id] = {
    "title": book_title,
    "author": book_author,
    "copies": book_copies
}
print("---------------------------------------------------------------------------------")
#Task 2: Remove a Book
# --------------------------------------------------
print("Remove a Book:")
#remove a book
book_id = input("Enter Book ID: ")
if book_id in library:
    del library[book_id]
    print("Book removed successfully.")
else:
    print("Book not found.")
print("---------------------------------------------------------------------------------")
#Task 3: Search a Book by ID
# --------------------------------------------------
print("Search a Book by ID:")
#search a book by id
book_id = input("Enter Book ID: ")
if book_id in library:
    book = library[book_id]
    print("Book ID:", book_id)
    print("Title:", book["title"])
    print("Author:", book["author"])
    print("Copies:", book["copies"])
else:
    print("Book not found.")
print("---------------------------------------------------------------------------------")
#Task 4: Search by Title
# --------------------------------------------------
print("Search by Title:")
#search a book by title
book_title = input("Enter Book Title: ")
for book_id, book in library.items():
    if book["title"] == book_title:
        print("Book ID:", book_id)
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Copies:", book["copies"])
        break
else:
    print("Book not found.")
print("---------------------------------------------------------------------------------")
#Task 5: Update Available Copies
# --------------------------------------------------
print("Update Available Copies:")
#update available copies
book_id = input("Enter Book ID: ")
if book_id in library:
    book = library[book_id]
    new_copies = int(input("Enter New Copies: "))
    book["copies"] = new_copies
    print("Copies updated successfully.")
else:
    print("Book not found.")
print("---------------------------------------------------------------------------------")
#Task 6: Issue a Book
# --------------------------------------------------
print("Issue a Book:")
#issue a book
book_id = input("Enter Book ID: ")
if book_id in library:
    book = library[book_id]
    if book["copies"] > 0:
        book["copies"] -= 1
        print("Book issued successfully.")
    else:
        print("Book is not available.")
else:
    print("Book not found.")
print("---------------------------------------------------------------------------------")
#Task 7: Return a Book
# --------------------------------------------------
print("Return a Book:")
#return a book
book_id = input("Enter Book ID: ")
if book_id in library:
    book = library[book_id]
    book["copies"] += 1
    print("Book returned successfully.")
else:
    print("Book not found.")
print("---------------------------------------------------------------------------------")
#Task 8: Display Books with Fewer than 3 Copies
# --------------------------------------------------
print("Display Books with Fewer than 3 Copies:")
#display books with fewer than 3 copies
for book_id, book in library.items():
    if book["copies"] < 3:
        print("Book ID:", book_id)
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Copies:", book["copies"])
        print("---------------------------------------------------------------------------------")
#Task 9: Display Books that are Unavailable
# --------------------------------------------------
print("Display Books that are Unavailable:")
#display books that are unavailable
for book_id, book in library.items():
    if book["copies"] == 0:
        print("Book ID:", book_id)
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Copies:", book["copies"])
        print("---------------------------------------------------------------------------------")
#Task 10: Find the Most Available Book
# --------------------------------------------------
print("Find the Most Available Book:")
#find the most available book
most_available_book = max(library, key=lambda x: library[x]["copies"])
print("Most Available Book:")
print("Book ID:", most_available_book)
print("Title:", library[most_available_book]["title"])
print("Author:", library[most_available_book]["author"])
print("Copies:", library[most_available_book]["copies"])
print("---------------------------------------------------------------------------------")
#Task 11: Generate a Restocking Report
# --------------------------------------------------
print("Generate a Restocking Report:")
#generate a restocking report
for book_id, book in library.items():
    if book["copies"] < 3:
        print("Book ID:", book_id)
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Copies:", book["copies"])
        print("---------------------------------------------------------------------------------")
#Task 12: Create a Separate Dictionary of Books Requiring Immediate Purchase
# --------------------------------------------------
print("Create a Separate Dictionary of Books Requiring Immediate Purchase:")
#create a separate dictionary of books requiring immediate purchase
immediate_purchase_books = {book_id: book for book_id, book in library.items() if book["copies"] == 0}#create a separate dictionary of books requiring immediate purchase
print("Books Requiring Immediate Purchase:")
for book_id, book in immediate_purchase_books.items():
    print("Book ID:", book_id)
    print("Title:", book["title"])
    print("Author:", book["author"])
    print("Copies:", book["copies"])
print("---------------------------------------------------------------------------------")
    