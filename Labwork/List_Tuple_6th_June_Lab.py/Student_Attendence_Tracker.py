'''6. Student Attendance Tracker
Problem Statement
Attendance for 15 days is recorded as:
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']
Write a program to:
• Count present and absent days. 
• Calculate attendance percentage. 
• Determine eligibility (minimum 75% attendance). 
• Display positions where the student was absent.'''
print("--- Student Attendance Tracker ---")
#given list of attendance
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']
#Count present and absent days
present_days = attendance.count('P') #counting present days
absent_days = attendance.count('A') #counting absent day
print("----------------------------------")
#Calculate attendance percentage
attendance_percentage = (present_days / (present_days + absent_days)) * 100 #attendance percentage = present days/total days*100
print("Attendance Percentage:", attendance_percentage)
print("----------------------------------")
#Determine eligibility (minimum 75% attendance)
if attendance_percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")
print("----------------------------------")
#Display positions where the student was absent
print("Positions where the student was absent:")
for i in range(len(attendance)):
    if attendance[i] == 'A': #checking if the student was absent
        print(i+1, end=" ") #position starts from 1 and index starts from 0
print() #new line
print("----------------------------------")
