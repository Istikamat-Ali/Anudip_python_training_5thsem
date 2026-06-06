'''Problem Statement
A company stores employee details in a tuple. Each employee record contains:
employees = (
 ("E101", "Anuj", 92),
 ("E102", "Rahul", 76),
 ("E103", "Priya", 58),
 ("E104", "Neha", 88),
 ("E105", "Amit", 45)
)
Where:
• First value = Employee ID 
• Second value = Employee Name 
• Third value = Performance Score 
Tasks
Write a Python program to:
1. Display details of employees scoring 80 or above. 
2. Count the number of employees who need improvement (score below 60). 
3. Find the employee with the highest score. 
4. Create a list containing the names of all employees scoring above 75. 
5. Display the performance category for each employee: 
o 90 and above → Excellent 
o 75 to 89 → Good 
o 60 to 74 → Average 
o Below 60 → Needs Improvement'''
#given tuple
employees = (
 ("E101", "Anuj", 92),
 ("E102", "Rahul", 76),
 ("E103", "Priya", 58),
 ("E104", "Neha", 88),
 ("E105", "Amit", 45)
)
#Task 1: To display details of employees scoring 80 or above.
print("----- Employee Records -----")
for record in employees:
  if(record[2] >= 80):#if performance score is 80 or above
    print("Employee ID : ",record[0])
    print("Name : ",record[1])
    print("Performance Score : ",record[2])
    print("---------------------------------")
#-----------------------------------------
#Task 2: To count the number of employees who need improvement
count = 0
for record in employees:
  if(record[2] < 60):#if performance score is less than 60
    count+=1
print("Number of employees need improvement : ",count)
print("------------------------------") 
#-----------------------------------------
#Task 3: Find the employee with the highest score
#initializing highest score record
highest_score = 0
for record in employees:
  if(record[2] > highest_score):#if performance score is greater than highest score
    highest_score = record[2]#update highest score
    highest_score_record = record#update highest score record
print("Employee with highest score : ")
print("Employee ID : ",highest_score_record[0])
print("Name : ",highest_score_record[1])
print("Performance Score : ",highest_score_record[2])
print("---------------------------------")
#-----------------------------------------
#Task 4: Create a list containing the names of all employees scoring above 75.
#taking an empty variable for names
names = []
for record in employees:
  if(record[2] > 75):#if performance score is greater than 75
    names.append(record[1])#add name to list
print("Names of employees scoring above 75 : ",names)
print("------------------------------")
print("----------------------------------")
#-----------------------------------------
#Task 5: Display the performance category for each employee
for record in employees:
  if(record[2] >= 90):#if performance score is 90 or above
    print("Employee ID : ",record[0])
    print("Name : ",record[1])
    print("Performance Category : Excellent")
  elif(record[2] >= 75 and record[2] < 90):#if performance score is between 75 and 90
    print("Employee ID : ",record[0])
    print("Name : ",record[1])
    print("Performance Category : Good")
  elif(record[2] >= 60 and record[2] < 75):#if performance score is between 60 and 75
    print("Employee ID : ",record[0])
    print("Name : ",record[1])
    print("Performance Category : Average")
  elif(record[2] < 60):#if performance score is less than 60
    print("Employee ID : ",record[0])
    print("Name : ",record[1])
    print("Performance Category : Needs Improvement")
  print("---------------------------------")