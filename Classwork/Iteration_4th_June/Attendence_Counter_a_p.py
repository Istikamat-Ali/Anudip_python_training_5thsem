#program to record student attendence and count present and absent student in the class
#initialize attendance count
attendance_count=0
#loop until attendance count is 30
while(attendance_count<=30): 
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
#display total attendance count
print("Total students present : ", attendance_count)
print("Total students absent : ", 30-attendance_count)