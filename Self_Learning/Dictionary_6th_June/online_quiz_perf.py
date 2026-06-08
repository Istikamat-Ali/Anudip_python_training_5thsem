'''8. Online Quiz Performance
Sample Data
quiz_scores = {
 "S001": 18,
 "S002": 12,
 "S003": 9,
 "S004": 20,
 "S005": 14,
 "S006": 7,
 "S007": 16,
 "S008": 10,
 "S009": 19,
 "S010": 13
}
(Quiz is out of 20 marks.)
Tasks
• Display students scoring 15 or above. 
• Count students scoring below 10. 
• Find the top performer. 
• Create a list of students who passed (≥ 10 marks). 
• Calculate the class average.'''
print("---------------------- Online Quiz Performance ----------------------")
#given dictionary
quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}
#Display students scoring 15 or above
print("Students scoring 15 or above:")
for student, score in quiz_scores.items():
    if score >= 15:
        print(student)
print("---------------------------------------------------------------------------------")
#Count students scoring below 10
count = 0
for student, score in quiz_scores.items():
    if score < 10:
        count += 1
print("Number of students scoring below 10:",count)
print("---------------------------------------------------------------------------------")
#Find the top performer
top_performer = max(quiz_scores, key=quiz_scores.get)#top performer is the key of the maximum value
print("Top Performer:",top_performer)
print("---------------------------------------------------------------------------------")
#Create a list of students who passed (≥ 10 marks)
passed_students = []
for student, score in quiz_scores.items():
    if score >= 10:
        passed_students.append(student)
print("Students who passed (>= 10 marks):",passed_students)
print("---------------------------------------------------------------------------------")
#Calculate the class average
average_score = sum(quiz_scores.values()) / len(quiz_scores)
print("Class Average:",average_score)
print("---------------------------------------------------------------------------------")
