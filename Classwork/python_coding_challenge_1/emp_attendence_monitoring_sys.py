'''Problem 6: Employee Attendance Monitoring System
Problem Statement
Employee attendance records are stored in attendance.txt.
Sample Input/Data (attendance.txt)
EMP101,P
EMP102,A
EMP103,P
EMP104,P
EMP105,A
EMP106,P
EMP107,P
EMP108,A
EMP109,P
EMP110,P
Tasks
1. Count present and absent employees. 
2. Display absent employee IDs. 
3. Calculate attendance percentage. 
4. Generate an absentee report in absent_report.txt. 
5. Display employees eligible for attendance awards (100% attendance). 
Sample Output
Present Employees: 7
Absent Employees: 3
Absent Employee IDs:
EMP102
EMP105
EMP108
Attendance Percentage: 70.0%
Absentee Report Generated Successfully.
Attendance Award Eligibility:
Not Applicable'''
#1. Count present and absent employees
with open("attendance.txt", "r") as file:
    lines = file.readlines()
    present_count = 0
    absent_count = 0
    for line in lines:
        if line.strip().split(",")[1] == "P":# for present list 1st index is compared with P
            present_count += 1
        else:
            absent_count += 1
    print("Present Employees:", present_count)
    print("Absent Employees:", absent_count)
#Display absent employee IDs
print("Absent Employee IDs:")
with open("attendance.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if line.strip().split(",")[1] == "A":# for absent list 1st index is compared with A
            print(line.strip().split(",")[0])#for absent employee id 0th index is printed
#calculate attendance percentage
with open("attendance.txt", "r") as file:
    lines = file.readlines()
    present_count = 0
    for line in lines:
        if line.strip().split(",")[1] == "P":# for present list 1st index is compared with P
            present_count += 1
    attendance_percentage = (present_count / len(lines)) * 100
    print("Attendance Percentage:", attendance_percentage)
#Generate an absentee report in absent_report.txt
with open("absent_report.txt", "w") as file:
    with open("attendance.txt", "r") as file1:
        lines = file1.readlines()
        for line in lines:
            if line.strip().split(",")[1] == "A":# for absent list 1st index is compared with A
                file.write(line)
    print("Absentee Report Generated Successfully.")
#Display employees eligible for attendance awards (100% attendance)
with open("attendance.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if line.strip().split(",")[1] == "P":# for present list 1st index is compared with P
            employee_id = line.strip().split(",")[0]
            print(f"Attendance Award Eligibility: {employee_id}")
        else:
            print(f"Not Applicable: {employee_id}")
