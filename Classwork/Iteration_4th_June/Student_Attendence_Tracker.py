# A teacher is recording attendance as students enter the classroom. The class strength is 30 students.
# Write a program that inputs whether Student is Present or Absent. Display total number of student present as well as absent.
# Sample Output
# Student 1
# Attendance : Present
# Student 2
# Attendance : Absent
# ...
# No. of Students Present : 20
# No. of Students Absent : 10
#program to record student attendence and count present and absent student in the class
#initialize attendance count
attendance_count=0
student_number=1
#loop until attendance count is 30
while(attendance_count<=30):
    print("Student ", student_number)
    #input of student attendence
    attendence=input("Is the student present (Y/N) : ")
    #check attendence and update attendance count
    if(attendence=="Y" or attendence=="y"):
        attendance_count+=1
        print("Student is present ... Attendance count : ", attendance_count)
        print("Student is absent ... Attendance count : ", 30-attendance_count)
    elif(attendence=="N" or attendence=="n"):
        print("Student is absent ... Attendance count : ", 30-attendance_count)
        print("Student is present ... Attendance count : ", attendance_count)
    else:
        print("Invalid input ... Exited")
        exit()
    student_number+=1
#display total attendance count
print("Total students present : ", attendance_count)
print("Total students absent : ", 30-attendance_count)  