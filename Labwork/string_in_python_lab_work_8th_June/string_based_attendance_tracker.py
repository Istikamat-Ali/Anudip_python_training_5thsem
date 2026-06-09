'''8. String-Based Attendance Tracker
Problem Statement
Attendance of a student for 15 days is represented as:
PPAPPPAAPPPPAPP
Where:
• P = Present 
• A = Absent 
Tasks
Write a program to:
1. Count Present and Absent days. 
2. Calculate attendance percentage. 
3. Find the longest consecutive streak of Presence. 
4. Find the longest consecutive streak of Absence. 
5. Determine whether attendance is below 75%. 
Sample Output
Attendance Record:
PPAPPPAAPPPPAPP
Present Days: 11
Absent Days: 4
Attendance Percentage: 73.33%
Longest Present Streak: 4
Longest Absent Streak: 2
Attendance Status: Below 75%'''
print("------------------ Attendance Record ------------------")
#input: attendance of 15 days
attendance = "PPAPPPAAPPPPAPP"
print("--------------------------------------------------")
#count present and absent days
present_days = attendance.count("P")
print("Present Days:", present_days)
print("---------------------------------------------------")
absent_days = attendance.count("A")
print("Absent Days:", absent_days)
print("---------------------------------------------------")
#calculate attendance percentage
attendance_percentage = (present_days / (present_days + absent_days)) * 100#for calculating percentage
print("Attendance Percentage:", attendance_percentage)
print("---------------------------------------------------")
#find the longest consecutive streak of Presence
present_streak = 0
current_streak = 0
for i in range(len(attendance)):
    if attendance[i] == "P":
        current_streak += 1
        if current_streak > present_streak:
            present_streak = current_streak
    else:
        current_streak = 0
print("Longest Present Streak:", present_streak)
print("---------------------------------------------------")
#find the longest consecutive streak of Absence
absent_streak = 0
current_streak = 0
for i in range(len(attendance)):
    if attendance[i] == "A":
        current_streak += 1
        if current_streak > absent_streak:
            absent_streak = current_streak
    else:
        current_streak = 0
print("Longest Absent Streak:", absent_streak)
print("---------------------------------------------------")
#determine whether attendance is below 75%
if attendance_percentage < 75:
    print("Attendance Status: Below 75%")
else:
    print("Attendance Status: Above 75%")
print("---------------------------------------------------")

