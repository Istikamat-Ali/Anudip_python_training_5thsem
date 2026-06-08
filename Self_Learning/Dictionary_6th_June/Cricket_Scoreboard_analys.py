'''4. Cricket Scoreboard Analysis
Sample Data
scores = {
 "Virat": 78,
 "Rohit": 112,
 "Gill": 45,
 "Rahul": 89,
 "Hardik": 32,
 "Jadeja": 61,
 "Surya": 105,
 "Pant": 95,
 "Bumrah": 18,
 "Shami": 25
}
Tasks
• Display players who scored 50 or more runs. 
• Count the number of centuries. 
• Find the player with the highest score. 
• Create a list of players scoring below 30 runs. 
• Determine how many players scored between 50 and 99. '''
print("--------------------- Cricket Scoreboard Analysis ---------------------")
#Given dictionary
scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}
print("------------------------------------------------------------------------")
#Display players who scored 50 or more runs
for player,score in scores.items():
    if score>=50:
        print("Player:",player,"Score:",score)
print("------------------------------------------------------------------------")
#Count the number of centuries
centuries = 0
for score in scores.values():
    if score >= 100:
        centuries += 1
print("Number of centuries:",centuries)
print("------------------------------------------------------------------------")
#Find the player with the highest score
highest_score = max(scores.values())
for player,score in scores.items():
    if score == highest_score:
        print("Player with highest score:",player)
print("------------------------------------------------------------------------")
#Create a list of players scoring below 30 runs
score_below_30 = []
for player,score in scores.items():
    if score < 30:
        score_below_30.append(player)
print("Players scoring below 30 runs:",score_below_30)
print("------------------------------------------------------------------------")
#Determine how many players scored between 50 and 99
score_between_50_99 = 0
for score in scores.values():
    if score >= 50 and score <= 99:
        score_between_50_99 += 1
print("Number of players scoring between 50 and 99 runs:",score_between_50_99)
print("------------------------------------------------------------------------")