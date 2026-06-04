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
s1_marks = float(input("Enter marks for Subject 1: "))
s2_marks = float(input("Enter marks for Subject 2: "))
s3_marks = float(input("Enter marks for Subject 3: "))
s4_marks = float(input("Enter marks for Subject 4: "))
s5_marks = float(input("Enter marks for Subject 5: "))
# validating the input
if (s1_marks < 0 or s1_marks > 100 or
    s2_marks < 0 or s2_marks > 100 or
    s3_marks < 0 or s3_marks > 100 or
    s4_marks < 0 or s4_marks > 100 or
    s5_marks < 0 or s5_marks > 100):
    exit("Marks should be between 0 and 100 ...Exited")
print("-------------------------------------------------------------")
# calculating total marks and percentage
total_marks = s1_marks + s2_marks + s3_marks + s4_marks + s5_marks
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
if s1_marks < 40:
    failed_subjects += 1
if s2_marks < 40:
    failed_subjects += 1
if s3_marks < 40:
    failed_subjects += 1
if s4_marks < 40:
    failed_subjects += 1
if s5_marks < 40:
    failed_subjects += 1            
# displaying the result
print("Total Marks:", total_marks)
print("Percentage: ",percentage)