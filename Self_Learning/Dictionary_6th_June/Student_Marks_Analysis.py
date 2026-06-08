'''1. Student Marks Analysis
Sample Data
marks = {
 "Aarav": 78,
 "Diya": 92,
 "Rohan": 45,
 "Ishita": 88,
 "Kabir": 56,
 "Meera": 39,
 "Arjun": 95,
 "Saanvi": 67,
 "Vivaan": 82,
 "Anaya": 51
}
Tasks
• Display students scoring 80 or above. 
• Count the number of students who failed (marks < 40). 
• Find the highest scorer. 
• Create a list of students scoring between 60 and 75. 
• Assign grades: 
o A: ≥ 90 
o B: 75–89 
o C: 50–74 
o F: < 50'''
print("--------------------------Student Marks Analysis-----------------------------")
#given dictionary
marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}
#Display students scoring 80 or above
print("Students Scoring 80 or Above:")
for student,mark in marks.items():
    if mark >= 80:
        print(f"{student} {mark}")
print("---------------------------------------------------------------------------------")
#Count the number of students who failed (marks < 40)
#initialize count variable to 0
failed_count = 0
#check marks less than 40   
for mark in marks.values():
    if mark < 40:
        failed_count += 1
print("Number of Failed Students:", failed_count)
print("---------------------------------------------------------------------------------")
#Find highest scorer
#initialize highest and lowest marks to first index or the list 
highest = list(marks.values())[0]
lowest = list(marks.values())[0]
#check marks greater than highest
for mark in marks.values():
    if mark > highest:
        highest = mark
#checking the lowest marks 
    if mark < lowest:
        lowest = mark
print("-------------------------------------------------------------------------------------")
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("-------------------------------------------------------------------------------------")
#Create a new list containing marks between 60 and 75
#taking an empty list for marks between 60 and 75
between_60_75 = []
#check marks between 60 and 75
for mark in marks.values():
    if mark > 60 and mark < 75:
        between_60_75.append(mark)
print("Marks between 60 and 75:", between_60_75)
print("-------------------------------------------------------------------------------------")
#Assign grades
#taking an empty list for grades
grades = []
#check marks between 60 and 75
for mark in marks.values():
    if mark > 90:
        grades.append("A")
    elif mark > 75 and mark < 90:
        grades.append("B")
    elif mark > 50 and mark < 75:
        grades.append("C")
    else:
        grades.append("F")
print("Grades:", grades)    
print("-------------------------------------------------------------------------------------")
