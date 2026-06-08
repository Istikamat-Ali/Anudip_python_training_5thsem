'''4. Cricket Tournament Statistics
Problem Statement
Runs scored by players in a tournament:
runs = {
 "Virat": 645,
 "Rohit": 512,
 "Gill": 698,
 "Rahul": 435,
 "Hardik": 278,
 "Pant": 534,
 "Surya": 389,
 "Jadeja": 301,
 "Iyer": 455,
 "KL": 410
}
Tasks
1. Display players scoring more than 500 runs. 
2. Find the Orange Cap winner. 
3. Find the lowest scorer. 
4. Calculate total runs scored. 
5. Create a list of players scoring below 400. 
6. Count players scoring between 400 and 600 runs. 
Sample Output
Players Scoring More Than 500 Runs:
Virat
Rohit
Gill
Pant
Orange Cap Winner: Gill (698)
Lowest Scorer: Hardik (278)
Total Tournament Runs: 4657
Players Scoring Below 400:
['Hardik', 'Surya', 'Jadeja']
Players Between 400 and 600 Runs: 5'''
print("---------------------Cricket Tournament Statistics---------------------")
#Given dictionary
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}
print("------------------------------------------------------------------------")
#Display players scoring more than 500 runs
print("Players scoring more than 500 runs:")
for player,runs in runs.items():
    if runs > 500:
        print(player)
print("------------------------------------------------------------------------")
#Find the Orange Cap winner
print("Orange Cap Winner:",max(runs))#orange cap winner is who score most
print("------------------------------------------------------------------------")
#Find the lowest scorer
print("Lowest Scorer:",min(runs))#lowest scorer is who score least
print("------------------------------------------------------------------------")
#Calculate total runs scored
print("Total tournament runs:",sum(runs))
print("------------------------------------------------------------------------")
#Create a list of players scoring below 400
print("Players scoring below 400 runs:")
for player,runs in runs.items():
    if runs < 400:
        print(player)
print("------------------------------------------------------------------------")
#Count players scoring between 400 and 600 runs
print("Players scoring between 400 and 600 runs:",len([runs for runs in runs.values() if 400 <= runs <= 600]))#gives number of runs between 400 and 600
print("------------------------------------------------------------------------")