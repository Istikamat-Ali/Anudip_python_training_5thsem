'''Problem 7: Cricket Tournament Statistics
Problem Statement
Runs scored by players in a tournament are given below.
Sample Data
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
1. Find the Orange Cap winner. 
2. Find the lowest scorer. 
3. Calculate total runs scored. 
4. Display players scoring more than 500 runs. 
5. Create a list of players scoring below 400. 
Sample Output
Orange Cap Winner:
Gill (698 runs)
Lowest Scorer:
Hardik (278 runs)
Total Runs: 4657
Players Scoring Above 500:
Virat
Rohit
Gill
Pant
Players Scoring Below 400:
['Hardik', 'Surya', 'Jadeja']'''
#given dictionary for name and scores
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
#find the orange cap winner
print("Orange Cap Winner:")
orange_cap_winner_runs=max(runs.values())
for player,runs in runs.items():
    if runs==orange_cap_winner_runs:
        orange_cap_winner=player
        print(orange_cap_winner,"(",runs,"runs)")
        break
print()
#find the lowest scorer
print("Lowest Score:")
lowest_scorer = min(runs.values())
for player,runs in runs.items():
    if runs == lowest_scorer:
        lowest_scorer_player = player
        print(lowest_scorer_player, "(", runs, "runs)")
        break
print()
#calculate total runs
print("Total Runs:")
total_runs = sum(runs.values())
print(total_runs)
print()
#display players scoring more than 500 runs
print("Players Scoring Above 500:")
for player,runs in runs.items():
    if runs > 500:
        print(player)
print()
#Create a list of players scoring below 400
print("Players Scoring Below 400:")
players_below_400 = []
for player,runs in runs.items():
    if runs < 400:
        players_below_400.append(player)
print(players_below_400)
