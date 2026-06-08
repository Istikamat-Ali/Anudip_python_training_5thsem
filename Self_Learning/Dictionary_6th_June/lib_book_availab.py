''' 5. Library Book Availability
Sample Data
books = {
 "Python Basics": 5,
 "Data Structures": 0,
 "Machine Learning": 3,
 "Java Programming": 2,
 "DBMS": 0,
 "Operating Systems": 6,
 "Networking": 4,
 "Cloud Computing": 1,
 "Cyber Security": 0,
 "Web Development": 7
}
Tasks
• Display books that are currently unavailable. 
• Count the number of available books. 
• Find the book with the maximum copies. 
• Create a list of books having less than 3 copies. 
• Calculate the total number of books available.'''
print("--------------------------Library Book Availability-----------------------------")
#Given dictionary of books and their availability
books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}
#Display books that are currently unavailable
print("Unavailable Books:")
for book, copies in books.items():
    if copies == 0:
        print(book)
print("---------------------------------------------------------------------------------")
#Count the number of available books
available_books = 0
for copies in books.values():
    if copies > 0:
        available_books += 1
print("Number of Available Books:", available_books)
print("---------------------------------------------------------------------------------")
#Find the book with the maximum copies
max_copies = max(books.values())
max_copies_book = [book for book, copies in books.items() if copies == max_copies]#generator expression for max copies
print("Book with Maximum Copies:", max_copies_book)
print("---------------------------------------------------------------------------------")
#Create a list of books having less than 3 copies
less_than_3_copies = [book for book, copies in books.items() if copies < 3]# generator expression 
print("Books with Less than 3 Copies:", less_than_3_copies)
print("---------------------------------------------------------------------------------")
#Calculate the total number of books available
total_books = sum(books.values())
print("Total Number of Books Available:", total_books)
print("---------------------------------------------------------------------------------")