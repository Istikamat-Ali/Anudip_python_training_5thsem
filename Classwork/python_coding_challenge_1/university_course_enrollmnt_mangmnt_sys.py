'''Problem 9: University Course Enrollment Management System 
Problem Statement 
Student enrollment data for university courses is stored below. 
Sample Data 
enrollment = { 
    "Python": 45, 
    "Java": 38, 
    "Data Science": 52, 
    "Web Development": 34, 
    "Machine Learning": 41, 
    "Cloud Computing": 29, 
    "Cyber Security": 33, 
    "DBMS": 48, 
    "Networking": 26, 
    "Operating Systems": 37 
} 
Tasks 
1. Display courses having more than 40 enrollments.  
2. Find the most and least popular courses.  
3. Calculate total enrollments.  
4. Create lists:  
o High Demand (>40)  
o Medium Demand (30–40)  
o Low Demand (<30)  
5. Count courses requiring promotional activities (<35 enrollments).  
Sample Output 
Courses with More Than 40 Enrollments: 
Python 
Data Science 
Machine Learning 
DBMS 
 
Most Popular Course: 
Data Science (52 students) 
 
Least Popular Course: 
Networking (26 students) 
 
Total Enrollments: 383 
 
High Demand: 
['Python', 'Data Science', 'Machine Learning', 'DBMS'] 
 
Medium Demand: 
['Java', 'Web Development', 'Cyber Security', 'Operating Systems'] 
 
Low Demand: 
['Cloud Computing', 'Networking'] 
 
Courses Requiring Promotion: 3'''
print("------------------University Course Enrollment Management System------------------")
#given dictionary of courses and their enrollments
enrollment = {
    "Python": 45,
    "Java": 38,
    "Data Science": 52,
    "Web Development": 34,
    "Machine Learning": 41,
    "Cloud Computing": 29,
    "Cyber Security": 33,
    "DBMS": 48,
    "Networking": 26,
    "Operating Systems": 37
}
#display courses having more than 40 enrollments
print("Courses with More Than 40 Enrollments:")
for course in enrollment:
    if enrollment[course] > 40:
        print(course)
print()
#find the most and least popular courses
most_popular=None #variable to store most popular course and its enrollment as tuple
least_popular=None #variable to store least popular course and its enrollment as tuple
for course in enrollment:
    if most_popular is None or enrollment[course]>enrollment[most_popular[0]]:
        most_popular=(course,enrollment[course])
    if least_popular is None or enrollment[course]<enrollment[least_popular[0]]:
        least_popular=(course,enrollment[course])
print("Most Popular Course:")
print(most_popular[0], "(", most_popular[1], "students)")
print()
print("Least Popular Course:")
print(least_popular[0], "(", least_popular[1], "students)")
print()
#calculate total enrollments
total_enrollments=0
for course in enrollment:
    total_enrollments+=enrollment[course]
print("Total Enrollments:",total_enrollments)
print()
#Create lists: High Demand (>40), Medium Demand (30–40), Low Demand (<30)
high_demand=[]
medium_demand=[]
low_demand=[]
for course in enrollment:
    if enrollment[course]>40:
        high_demand.append(course)
    elif enrollment[course]>30:
        medium_demand.append(course)
    else:
        low_demand.append(course)
print("High Demand:")
print(high_demand)
print()
print("Medium Demand:")
print(medium_demand)
print()
print("Low Demand:")
print(low_demand)
print()
#Count courses requiring promotional activities (<35 enrollments)
count=0
for course in enrollment:
    if enrollment[course]<35:
        count+=1
print("Courses Requiring Promotion:",count)
   
