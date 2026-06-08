'''2. Employee Performance Dashboard
Problem Statement
Employee performance scores are stored as:
performance = {
 "EMP101": 92,
 "EMP102": 78,
 "EMP103": 45,
 "EMP104": 88,
 "EMP105": 97,
 "EMP106": 56,
 "EMP107": 81,
 "EMP108": 64,
 "EMP109": 39,
 "EMP110": 73
}
Tasks
1. Display employees scoring above 80. 
2. Count employees needing improvement (score < 60). 
3. Find the top performer. 
4. Calculate average performance score. 
5. Create separate lists: 
o Excellent (≥ 90) 
o Good (75–89) 
o Average (60–74) 
o Poor (< 60) 
Sample Output
Employees Scoring Above 80:
EMP101
EMP104
EMP105
EMP107
Top Performer: EMP105 (97)
Employees Needing Improvement: 3
Average Score: 71.3
Excellent:
['EMP101', 'EMP105']
Good:
['EMP102', 'EMP104', 'EMP107']
Average:
['EMP108', 'EMP110']
Poor:
['EMP103', 'EMP106', 'EMP109']'''
#given dictionary for employee performance scores
performance = {
 "EMP101": 92,
 "EMP102": 78,
 "EMP103": 45,
 "EMP104": 88,
 "EMP105": 97,
 "EMP106": 56,
 "EMP107": 81,
 "EMP108": 64,
 "EMP109": 39,
 "EMP110": 73
}
print("---------------- Employee Performance Dashboard ----------------")
print("---------------------------------")
#-----------------------------------------
#Task 1: Display employees scoring above 80
print("Employees Scoring Above 80:")
for key in performance:
  if(performance[key] > 80):
    print(key)
print("---------------------------------")
#-----------------------------------------
#Task 2: Count employees needing improvement
count = 0
for key in performance:
  if(performance[key] < 60):
    count+=1
print("Employees Needing Improvement:",count)
print("---------------------------------")
#-----------------------------------------
#Task 3: Find the top performer
print("Top Performer:")
#initializing top performer record
top_performer = 0
for key in performance:
  if(performance[key] > top_performer):
    top_performer = performance[key]
    top_performer_record = key
print(top_performer_record,"(",top_performer,")")
print("---------------------------------")
#-----------------------------------------
#Task 4: Calculate average performance score
print("Average Score:")
total = 0
for key in performance:
  total+=performance[key]
print(total/len(performance))
print("---------------------------------")
#-----------------------------------------
#Task 5: Create separate lists
print("Excellent:")
excellent = [key for key in performance if performance[key] >= 90]
print(excellent)
print("Good:")
good = [key for key in performance if performance[key] >= 75 and performance[key] < 90]
print(good)
print("Average:")
average = [key for key in performance if performance[key] >= 60 and performance[key] < 75]
print(average)
print("Poor:")
poor = [key for key in performance if performance[key] < 60]
print(poor)
print("---------------------------------")