'''Student Performance Analyzer
Problem Statement
A teacher has marks of students stored in a list.
marks = [78, 45, 92, 35, 88, 40, 99, 56]
Write a program to:
1. Display all passed students (marks ≥ 40). 
2. Count the number of failed students. 
3. Find the highest and lowest marks without using max() or min(). 
4. Create a new list containing marks above 75.'''
#Program to display all passed students,count no of failed students,highet and lowest marks and new list containing marks greater than 75
print("--------------------------Student Performance Analyzer-----------------------------")
#given list
marks = [78, 45, 92, 35, 88, 40, 99, 56]
#Display all passed students (marks >= 40)
print("Passed Students Marks:")
for mark in marks:
    if mark >= 40:
        print(mark, end=" ")
print("\n---------------------------------------------------------------------------------")
# Count the number of failed students
#initialize count variable to 0
failed_count = 0
#check marks less than 40
for mark in marks:
    if mark < 40:
        failed_count += 1
print("Number of Failed Students:", failed_count)
print("-----------------------------------------------------------------------------------")
#Find highest and lowest marks without using max() or min()
#initialize highest and lowest marks to first index or the list 
highest = marks[0]
lowest = marks[0]
#checking the highest marks
for mark in marks:
    if mark > highest:
        highest = mark
#checking the lowest marks 
    if mark < lowest:
        lowest = mark
print("-------------------------------------------------------------------------------------")
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("-------------------------------------------------------------------------------------")
#Create a new list containing marks above 75
#taking an empty list for marks greater than 75
above_75 = []
#check marks greater than 75
for mark in marks:
    if mark > 75:
        above_75.append(mark)
print("Marks Above 75:", above_75)

