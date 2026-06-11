'''Problem 4: School Report Card Generator
Problem Statement
Student marks are stored in marks.txt.
Sample Input/Data (marks.txt)
S101,Anuj,92
S102,Rahul,76
S103,Priya,88
S104,Neha,45
S105,Amit,58
S106,Sneha,95
S107,Karan,81
S108,Pooja,73
S109,Rohit,39
S110,Anjali,90
Tasks
1. Calculate grades for all students. 
2. Generate a report card file report_card.txt. 
3. Display topper details. 
4. Count pass and fail students. 
5. Display students eligible for merit certificates (marks ≥ 90). 
Sample Output
Topper:
Sneha (95)
Passed Students: 9
Failed Students: 1
Merit Certificate Holders:
Anuj
Sneha
Anjali
Report Cards Generated Successfully.'''
#calculate grade for all students
with open("marks.txt", "r") as file:
    for line in file:
        student_id, name, marks = line.strip().split(",")
        marks = int(marks)#marks is converted to integer for comparision of marks
        if marks >= 90:
            grade = "A"
        elif 75 <= marks < 90:
            grade = "B"
        elif 40 <= marks < 75:
            grade = "C"
        else:
            grade = "F"
        print(f"Name: {name}, Marks: {marks}, Grade: {grade}")
#generate a report card file report_card.txt
with open("report_card.txt", "w") as file:
    with open("marks.txt", "r") as file1:
        for line in file1:
            student_id, name, marks = line.strip().split(",")
            marks = int(marks)
            if marks >= 90:
                grade = "A"
            elif 75 <= marks < 90:
                grade = "B"
            elif 40 <= marks < 75:
                grade = "C"
            else:
                grade = "F"
            file.write(f"Name: {name}, Marks: {marks}, Grade: {grade}\n")
print("Report Cards Generated Successfully.")
#display toppers details 
with open("marks.txt","r") as file:
    max_marks = 0
    for line in file:
        student_id, name, marks = line.strip().split(",")
        marks = int(marks)
        if marks > max_marks:
            max_marks = marks
            topper_name = name
    print(f"Topper: {topper_name} ({max_marks})")
#count pass and fail students
with open("marks.txt", "r") as file:
    pass_count = 0
    fail_count = 0
    for line in file:
        _, _, marks = line.strip().split(",")
        marks = int(marks)
        if marks >= 40:
            pass_count += 1
        else:
            fail_count += 1
print(f"Passed Students: {pass_count}")
print(f"Failed Students: {fail_count}")
#display students eligible for merit certificates
print("Merit Certificate Holders:")
with open("marks.txt", "r") as file:
    for line in file:
        student_id, name, marks = line.strip().split(",")
        marks = int(marks)
        if marks >= 90:
            print(name)
