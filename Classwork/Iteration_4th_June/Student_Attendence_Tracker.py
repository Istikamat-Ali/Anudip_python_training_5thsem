#program to record student attendence and count present and absent student in the class
#input: attendance of 30 students (present/absent)
present = 0
absent = 0
student = 1
#loop to record attendance for 30 students
while student <= 30:
    print("\nStudent", student)
    attendance = input("Attendance (Present/Absent): ").lower()

    if attendance == "present":
        present += 1
    elif attendance == "absent":
        absent += 1
    else:
        print("Invalid Input! Counted as Absent.")
        absent += 1

    student += 1

print("\n--- Attendance Report ---")
print("No. of Students Present :", present)
print("No. of Students Absent :", absent) 