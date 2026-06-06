'''Problem Statement
A batsman's scores in different matches are stored in a list.
scores = [45, 78, 12, 100, 67, 8, 90, 55]
Write a program to:
• Count half-centuries and centuries. 
• Find the highest score. 
• Display all scores below 20. 
• Calculate the average score.
'''
print("--------------------- Cricket Tournamnt Scorecard ---------------------")
#given list
scores = [45, 78, 12, 100, 67, 8, 90, 55]
#count variables for half-centuries and centuries
half_centuries = 0
centuries = 0
for score in scores:
    if score >= 50 and score < 100:#for half-centuries
        half_centuries += 1
    elif score >= 100:#for centuries
        centuries += 1
#total count for half centuries and centuries
print("Half-centuries:", half_centuries)
print("Centuries:", centuries)
print("---------------------------------")
#finding the highest score  
highest_score = max(scores)
print("Highest Score:", highest_score)
print("---------------------------------")
#displaying all scores below 20
print("Scores below 20:")
for score in scores:
    if score < 20:
        print(score,end=" ")
print("\n---------------------------------")
#calculating average score
total_score = sum(scores)
average_score = total_score / len(scores)
print("Average Score:", average_score)
print("---------------------------------")