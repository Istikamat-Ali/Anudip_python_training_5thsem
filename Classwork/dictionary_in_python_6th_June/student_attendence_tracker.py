'''Create Attendance tracker of 30 students. Ask the user to input roll number of student and also 
input whether student is Present or Absent. Store the data in dictionary where roll number will 
be used as a key and Attendance as Value.
Display the roll number of students who are Present'''
print("--- Student Attendance Tracker ---")
# Dictionary to store attendance
attendance = {}
# Input attendance of 30 students
for i in range(30):
# Input roll number
    roll_no = int(input("Enter Roll Number: "))
# Input attendance status
    status = input("Enter Attendance (Present/Absent): ")
# Store roll number as key and attendance as value
    attendance[roll_no] = status
# Display present students
print("\nRoll Numbers of Present Students:")
# Traverse dictionary
for roll_no, status in attendance.items():
# Check if student is present
    if status.lower() == "present":
# Display roll number
        print(roll_no, end=" ")
 
