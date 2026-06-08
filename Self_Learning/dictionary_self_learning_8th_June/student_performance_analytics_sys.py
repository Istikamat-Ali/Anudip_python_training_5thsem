'''1. Student Performance Analytics System
Problem Statement
A coaching institute wants to analyze student performance.
Store details of at least 30 students in a dictionary.
Example Structure
students = {
 "S101": {"name": "Anuj", "marks": 85},
 "S102": {"name": "Rahul", "marks": 72}
}
Requirements
1. Display all student records. 
2. Search a student using Student ID. 
3. Add a new student. 
4. Update marks of an existing student. 
5. Delete a student. 
6. Find topper and lowest scorer. 
7. Calculate class average. 
8. Count pass and fail students. 
9. Generate grades: 
o A (90+) 
o B (75–89) 
o C (50–74) 
o F (<50) 
10. Display students scoring above average. 
11. Display top 5 performers. 
12. Create a separate dictionary for scholarship students (marks > 85). 
Expected Learning
• Nested Dictionaries 
• Dictionary Traversal 
• Searching 
• Aggregation 
• Report Generation'''
print("----------------------------Student Performance Analytics System-----------------------------")
#store details of at least 30 students in a dictionary from user
students = {}
for i in range(30):
    #for roll_no like S101 take roll_no input from user in the format S101
    roll_no =input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    students[roll_no] = {"name": name, "marks": marks}
print("----------------------------------------------------------------------")
#display all student records
print("\nAll Student Records:")
for roll_no, student in students.items():
    print("Roll Number:", roll_no)
    print("Name:", student["name"])
    print("Marks:", student["marks"])
print("----------------------------------------------------------------------")
#search a student using student id
print("\nSearch a Student:")
roll_no = input("Enter Roll Number to Search: ")
if roll_no in students:
    student = students[roll_no]
    print("Name:", student["name"])
    print("Marks:", student["marks"])
else:
    print("Student not found.")
print("----------------------------------------------------------------------")
#add a new student
print("\nAdd a New Student:")
roll_no = input("Enter Roll Number: ")
name = input("Enter Name: ")
marks = int(input("Enter Marks: "))
students[roll_no] = {"name": name, "marks": marks}
print("Student added successfully.")
print("----------------------------------------------------------------------")
#update marks of an existing student
print("\nUpdate Marks:")
roll_no = input("Enter Roll Number: ")
if roll_no in students:
    marks = int(input("Enter Updated Marks: "))
    students[roll_no]["marks"] = marks#update marks
    print("Marks updated successfully.")
else:
    print("Student not found.")
print("----------------------------------------------------------------------")
#delete a student
print("\nDelete a Student:")
roll_no = input("Enter Roll Number: ")
if roll_no in students:
    del students[roll_no]
    print("Student deleted successfully.")
else:
    print("Student not found.")
print("----------------------------------------------------------------------")
#find topper and lowest scorer
print("\nFind Topper and Lowest Scorer:")
topper = None
lowest_scorer = None
for roll_no, student in students.items():
    if topper is None or student["marks"] > students[topper]["marks"]:
        topper = roll_no
    if lowest_scorer is None or student["marks"] < students[lowest_scorer]["marks"]:
        lowest_scorer = roll_no
print("Topper:", students[topper]["name"])
print("Lowest Scorer:", students[lowest_scorer]["name"])
print("----------------------------------------------------------------------")
#calculate class average
print("\nCalculate Class Average:")
total_marks = 0
for student in students.values():
    total_marks += student["marks"]
average = total_marks / len(students)
print("Class Average:", average)
print("----------------------------------------------------------------------")
#count pass and fail students
print("\nCount Pass and Fail Students:")
pass_count = 0
fail_count = 0
for student in students.values():
    if student["marks"] >= 50:
        pass_count += 1
    else:
        fail_count += 1
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)
print("----------------------------------------------------------------------")
#generate grades
print("\nGenerate Grades:")
for roll_no, student in students.items():
    if student["marks"] >= 90:
        grade = "A"
    elif student["marks"] >= 75:
        grade = "B"
    elif student["marks"] >= 50:
        grade = "C"
    else:
        grade = "F"
    print("Roll Number:", roll_no)
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("Grade:", grade)
print("----------------------------------------------------------------------")
#display students scoring above average
print("\nStudents Scoring Above Average:")
for roll_no, student in students.items():
    if student["marks"] > average:
        print("Roll Number:", roll_no)
        print("Name:", student["name"])
        print("Marks:", student["marks"])
print("----------------------------------------------------------------------")
#display top 5 performers
print("\nTop 5 Performers:")
sorted_students = sorted(students.items(), key=lambda x: x[1]["marks"], reverse=True)
top_5 = sorted_students[:5]
for roll_no, student in top_5:
    print("Roll Number:", roll_no)
    print("Name:", student["name"])
    print("Marks:", student["marks"])
print("----------------------------------------------------------------------")
#store details of at least 30 students in a dictionary from user
print("\nCreate a Separate Dictionary for Scholarship Students (Marks > 85):")
scholarship_students = {}
for i in range(30):
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    if marks > 85:
        scholarship_students[roll_no] = {"name": name, "marks": marks}
#display scholarship students
print("\n---------------------------Scholarship Students:----------------------------")
for roll_no, student in scholarship_students.items():
    print("Roll Number:", roll_no)
    print("Name:", student["name"])
    print("Marks:", student["marks"])
print("----------------------------------------------------------------------")

