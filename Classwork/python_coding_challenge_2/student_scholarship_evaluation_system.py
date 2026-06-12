'''Problem 2: Student Scholarship Evaluation System 
Problem Statement 
The marks obtained by students in the final examination are stored as follows: 
Sample Data 
marks = { 
    "Anuj": 92, 
    "Rahul": 76, 
    "Priya": 88, 
    "Neha": 64, 
    "Amit": 58, 
    "Sneha": 95, 
    "Karan": 81, 
    "Pooja": 73, 
    "Rohit": 47, 
    "Anjali": 90 
} 
Tasks 
1. Display students scoring above 85 marks.  
2. Find the topper.  
3. Find the student with the lowest marks.  
4. Calculate class average marks.  
5. Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  
6. Create a list of scholarship students (marks ≥ 90).  
Sample Output 
Students Scoring Above 85: 
Anuj 
Priya 
Sneha 
Anjali 
 
Topper: 
Sneha (95) 
 
Lowest Scorer: 
Rohit (47) 
 
Average Marks: 76.4 
 
Scholarship Students: 
['Anuj', 'Sneha', 'Anjali']'''
print("-----------Student Scholarship Evaluation System-----------")
#given dictionary of name of students and marks
marks = {
    "Anuj": 92,
    "Rahul": 76,
    "Priya": 88,
    "Neha": 64,
    "Amit": 58,
    "Sneha": 95,
    "Karan": 81,
    "Pooja": 73,
    "Rohit": 47,
    "Anjali": 90
}
#display students scoring above 85 marks
print("\nStudents Scoring Above 85:")
for student, marks in marks.items():
    if marks > 85:
        print(student)
print()
#find the topper student 
for student, marks in marks.items():
    if marks == max(marks.values()):
        print("Topper:\n", student)
        break  # break is used to exit the loop once the topper is found
print()
#find the student with the lowest marks
for student, marks in marks.items():
    if marks == min(marks.values()):
        print("Lowest Scorer:\n", student)
        break  # break is used to exit the loop once the lowest scorer is found
print()
#calculate class average marks
total_marks = sum(marks.values())
average_marks = total_marks / len(marks)
print("Average Marks:", average_marks)
print() 
#generate grades
print("Grades:")
for student, marks in marks.items():
    if marks >= 90:
        print(student, "(A)")
    elif 75 <= marks < 90:
        print(student, "(B)")
    elif 50 <= marks < 75:
        print(student, "(C)")
    else:
        print(student, "(F)")
print()
#Create a list of scholarship students (marks >= 90)
scholarship_students = [student for student, marks in marks.items() if marks >= 90]# list comprehension for creating a list
print("Scholarship Students:")
print(scholarship_students)