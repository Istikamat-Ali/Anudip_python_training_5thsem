# Problem Statement:
# Accept marks of 5 subjects.
# Display:
# • Total Marks 
# • Percentage 
# • Grade 
# Grade Criteria:
# Percentage Grade
# >=90 A+
# >=75 A
# >=60 B
# >=40 C
# <40 Fail
# Also display the number of subjects failed.
#program to manage student results
print("---------------------Student Result Management System---------------------")
# input marks for 5 subjects from user
Physics_marks = float(input("Enter marks for Subject 1: "))
Chemistry_marks = float(input("Enter marks for Subject 2: "))
Mathematics_marks = float(input("Enter marks for Subject 3: "))
Biology_marks = float(input("Enter marks for Subject 4: "))
Computer_Science_marks = float(input("Enter marks for Subject 5: "))
# validating the input
if (Physics_marks < 0 or Physics_marks > 100 or
    Chemistry_marks < 0 or Chemistry_marks > 100 or
    Mathematics_marks < 0 or Mathematics_marks > 100 or
    Biology_marks < 0 or Biology_marks > 100 or
    Computer_Science_marks < 0 or Computer_Science_marks > 100):
    exit("Marks should be between 0 and 100 ...Exited")
print("-------------------------------------------------------------")
# calculating total marks and percentage
total_marks = Physics_marks + Chemistry_marks + Mathematics_marks + Biology_marks + Computer_Science_marks
percentage = (total_marks / 500) * 100
# determining grade based on percentage
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:   
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"
# counting number of subjects failed using for loop (without using list comprehension)
failed_subjects = 0
if Physics_marks < 40:
    failed_subjects += 1
if Chemistry_marks < 40:
    failed_subjects += 1
if Mathematics_marks < 40:
    failed_subjects += 1
if Biology_marks < 40:
    failed_subjects += 1
if Computer_Science_marks < 40:
    failed_subjects += 1            
# displaying the result
print("Total Marks:", total_marks)
print("Percentage: ",percentage)
print("Grade:", grade)
print("Number of Subjects Failed:", failed_subjects)    