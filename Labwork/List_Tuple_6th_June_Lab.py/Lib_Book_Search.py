'''Problem Statement
Books available in a library:
books = [
 ("Python Basics", 5),
 ("Data Science", 0),
 ("Java Programming", 3),
 ("Machine Learning", 0)
]
Write a program to:
• Display unavailable books. 
• Find all books with more than 2 copies. 
• Count available books. 
• Stop searching once a requested book is found.
'''
print("---------------------- Lib Book Search ----------------------")
# List of books and their availability
books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]
# Display unavailable books
print("Unavailable Books:")
for book, copies in books:
    if copies == 0:
        print(book)
print("---------------------------------")
#-----------------------------------------
#Find all books with more than 2 copies
print("Books with more than 2 copies:")
for book, copies in books:
    if copies > 2:
        print(book)
print("---------------------------------")
#-----------------------------------------
#Count available books
available_books = 0
for book, copies in books:
    if copies > 0:
        available_books += 1
print("Available Books:", available_books)
print("---------------------------------")
#-----------------------------------------
#Stop searching once a requested book is found
requested_book = "Python Basics"
for book, copies in books:
    if book == requested_book:
        print("Book found:", book)
        break   #breaking the loop
    else:
        print("Book not found:", book)
print("---------------------------------")
#-----------------------------------------  
