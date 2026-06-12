'''Problem 6: Library Book Availability System
Problem Statement
The number of available copies of books in a library is stored below.
Sample Data
books = {
 "Python": 5,
 "Java": 2,
 "DBMS": 4,
 "Networking": 1,
 "OS": 3,
 "AI": 6,
 "ML": 2,
 "Cloud": 5,
 "Cyber Security": 1,
 "Web Development": 4
}
Tasks
1. Display books with fewer than 3 copies. 
2. Find the book with maximum copies. 
3. Find the book with minimum copies. 
4. Count total books available. 
5. Generate a restocking list. 
Sample Output
Books Requiring Attention:
Java
Networking
ML
Cyber Security
Book with Maximum Copies:
AI (6 copies)
Book with Minimum Copies:
Networking (1 copy)
Total Copies Available: 33
Restocking List:
['Java', 'Networking', 'ML', 'Cyber Security']'''
print("------------------Library Book Availability System------------------")
#Given dictionary of books and their availability
books = {
    "Python": 5,
    "Java": 2,
    "DBMS": 4,
    "Networking": 1,
    "OS": 3,
    "AI": 6,
    "ML": 2,
    "Cloud": 5,
    "Cyber Security": 1,
    "Web Development": 4
}
#Task 1: Display books with fewer than 3 copies
print("Books Requiring Attention:")
for book, copies in books.items():
    if copies < 3:
        print(book)
print()
#Task 2: Find the book with maximum copies
max_copies_book = max(books.values)
for book, copies in books.items():
    if copies == max_copies_book:
        max_copies_book = book
print("Book with Maximum Copies:")
print(max_copies_book, "(", books[max_copies_book], "copies)")
print()
#Task 3: Find the book with minimum copies
min_copies_book = min(books, key=books.get)
print("Book with Minimum Copies:")
print(min_copies_book, "(", books[min_copies_book], "copies)")
print()
#Task 4: Count total books available
total_copies = sum(books.values())
print("Total Copies Available:", total_copies)
print()
#Task 5: Generate a restocking list for copies less than or  equal to 2
restocking_list = [book for book, copies in books.items() if copies < 3]#list comprehension is used to create a new list
print("Restocking List:")
print(restocking_list) 