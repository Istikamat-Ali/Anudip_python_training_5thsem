'''Constraints
• Use functions to modularize the program. 
• Use file handling (open(), read(), write(), append()). 
• Use lists/dictionaries wherever appropriate. 
• Do not use databases or external libraries. 
• Implement menu-driven execution using a while loop. 
• Ensure that updates are reflected in the original file.
3. Student Result Processing System
Problem Statement
Student marks are stored in results.txt.
File Format
S101,Anuj,85
S102,Rahul,72
S103,Priya,96
S104,Neha,68
S105,Amit,39
S106,Sneha,54
S107,Karan,91
S108,Pooja,78
S109,Rohit,47
S110,Anjali,88
Requirements
Write a program to:
1. Display all student records. 
2. Search a student using Student ID. 
3. Find topper and lowest scorer. 
4. Calculate class average. 
5. Count pass and fail students. 
6. Generate grades: 
o A (90+) 
o B (75–89) 
o C (40–74) 
o F (<40) 
7. Write grade reports into a new file named grades.txt.'''
print("---------------------Student Result Processing System---------------------")
#function for displaying all student records
def display_all_students():
    with open("results.txt", "r") as file:
        for line in file:
            print(line.strip()) #strip is used to remove new line character
#function for searching a student using student id
def search_student(student_id):
    with open("results.txt", "r") as file:
        for line in file:
            if line.startswith(student_id):
                return line # returning the line if student id is found
    return None
#function for finding topper and lowest scorer
def find_topper_lowest_scorer():    
    highest_scorer = None # variable to store highest scorer and its marks as tuple
    lowest_scorer = None # variable to store lowest scorer and its marks as tuple
    with open("results.txt", "r") as file:
        for line in file:
            student_id, _, marks = line.strip().split(",")
            marks = int(marks)
            if highest_scorer is None or marks > highest_scorer[1]:# if highest scorer is None or marks of student is greater than highest scorer
                highest_scorer = (student_id, marks) #update highest scorer
            if lowest_scorer is None or marks < lowest_scorer[1]:
                lowest_scorer = (student_id, marks)
    return highest_scorer, lowest_scorer
#function for calculating class average
def calculate_class_average():
    total_marks = 0
    student_count = 0
    with open("results.txt", "r") as file:
        for line in file:
            _, _, marks = line.strip().split(",")# for splitting line by comma of form list of strings 
            marks = int(marks)
            total_marks += marks
            student_count += 1
    return total_marks / student_count
#function for counting pass and fail students
def count_pass_fail_students():
    pass_count = 0
    fail_count = 0
    with open("results.txt", "r") as file:
        for line in file:
            _, _, marks = line.strip().split(",")
            marks = int(marks)
            if marks >= 40:
                pass_count += 1
            else:
                fail_count += 1
    return pass_count, fail_count
#function for generating grades
def generate_grades():
    with open("results.txt", "r") as file:
        for line in file:
            student_id, _, marks = line.strip().split(",")
            marks = int(marks) #converting to integer for comparison
            if marks >= 90:
                grade = "A"
            elif 75 <= marks < 90:
                grade = "B"
            elif 40 <= marks < 75:
                grade = "C"
            else:
                grade = "F"
            print(f"Student ID: {student_id}, Marks: {marks}, Grade: {grade}")
            with open("grades.txt", "a") as grade_file:
                grade_file.write(f"Student ID: {student_id}, Marks: {marks}, Grade: {grade}\n")
#calling functions
display_all_students()
student_id = input("Enter student ID to search: ")
result = search_student(student_id)
if result:
    print(result)
else:
    print("Student not found.")
topper, lowest_scorer = find_topper_lowest_scorer()
print(f"Topper: {topper[0]}, Marks: {topper[1]}")
print(f"Lowest Scorer: {lowest_scorer[0]}, Marks: {lowest_scorer[1]}")
average = calculate_class_average()
print(f"Class Average: {average}")
pass_count, fail_count = count_pass_fail_students()
print(f"Pass Count: {pass_count}, Fail Count: {fail_count}")
generate_grades()
           