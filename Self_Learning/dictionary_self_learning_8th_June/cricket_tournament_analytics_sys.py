'''4. Cricket Tournament Analytics System
Problem Statement
Store statistics of at least 30 cricket players.
Example Structure
players = {
 "Virat": {
 "runs": 645,
 "matches": 12,
 "wickets": 0
 }
}
Requirements
1. Display all player statistics. 
2. Find highest run scorer. 
3. Find lowest run scorer. 
4. Calculate average runs. 
5. Find player with maximum wickets. 
6. Find all-rounders (runs > 300 and wickets > 5). 
7. Display players scoring above average. 
8. Create categories: 
o Star Performer 
o Good Performer 
o Average Performer 
o Poor Performer 
9. Generate team statistics. 
10. Display top 5 batsmen. 
11. Display top 5 bowlers. 
12. Create a separate dictionary for award winners. 
Challenge
Generate a tournament report.'''
print("------- Cricket Tournament Analytics System -------")
# taking input from user in this format
'''players = {
 "Virat": {
 "runs": 645,
 "matches": 12,
 "wickets": 0
 }
}
'''
players={}
for i in range(11):
    player_name=input("Enter the name of player " + str(i+1) + ": ")
    runs=int(input("Enter the number of runs scored by " + player_name + ": "))
    matches=int(input("Enter the number of matches played by " + player_name + ": "))
    wickets=int(input("Enter the number of wickets taken by " + player_name + ": "))
    players[player_name]={"runs":runs,"matches":matches,"wickets":wickets}
#display the player statistics
print("\nPlayer Statistics: ")
for player_name,player in players.items():
    print("Player:",player_name)
    print("Runs:",player["runs"])
    print("Matches:",player["matches"])
    print("Wickets:",player["wickets"])
print("---------------------------------------------------------------------------------")
#finding the highest run scorer
print("Highest Run Scorer: ")
highest_run_scorer=""
highest_runs=0
for player_name,player in players.items():
    if player["runs"]>highest_runs:
        highest_run_scorer=player_name
        highest_runs=player["runs"]
print("The highest run scorer is:",highest_run_scorer)
print("---------------------------------------------------------------------------------")
#finding the lowest run scorer
print("Lowest Run Scorer: ")
lowest_run_scorer=""
lowest_runs=1000
for player_name,player in players.items():
    if player["runs"]<lowest_runs:
        lowest_run_scorer=player_name
        lowest_runs=player["runs"]
print("The lowest run scorer is:",lowest_run_scorer)
print("---------------------------------------------------------------------------------")
#calculate the average runs
print("Average Runs: ")
total_runs=0
for player_name,player in players.items():
    total_runs+=player["runs"]
average_runs=total_runs/len(players)
print("Average Runs: ",average_runs)
print("---------------------------------------------------------------------------------")
#find the player with maximum wickets
print("Player with maximum wickets: ")
highest_wickets_player=""
highest_wickets=0
for player_name,player in players.items():
    if player["wickets"]>highest_wickets:
        highest_wickets_player=player_name
        highest_wickets=player["wickets"]
print("The player with maximum wickets is:",highest_wickets_player)
print("---------------------------------------------------------------------------------")
#find all-rounders (runs > 300 and wickets > 5)
print("All-rounders: ")
all_rounders=[]
for player_name,player in players.items():
    if player["runs"]>300 and player["wickets"]>5:
        all_rounders.append(player_name)
print("All-rounders: ",all_rounders)
print("---------------------------------------------------------------------------------")
#display players scoring above average
print("Players scoring above average: ")
for player_name,player in players.items():
    if player["runs"]>average_runs:
        print("Player:",player_name)
        print("Runs:",player["runs"])
        print("Matches:",player["matches"])
        print("Wickets:",player["wickets"])
print("---------------------------------------------------------------------------------")
#generate team statistics
team_runs=0
team_wickets=0
for player_name,player in players.items():
    team_runs+=player["runs"]
    team_wickets+=player["wickets"]
team_average_runs=team_runs/len(players)
team_average_wickets=team_wickets/len(players)
print("Team Statistics: ")
print("Runs:",team_runs)
print("Wickets:",team_wickets)
print("Average Runs:",team_average_runs)
print("Average Wickets:",team_average_wickets)
print("---------------------------------------------------------------------------------")
#display top 5 batsmen
print("Top 5 Batsmen: ")
batsmen=[]
for player_name,player in players.items():
    batsmen.append((player["runs"],player_name))
batsmen.sort(reverse=True)
for runs,name in batsmen[:5]:
    print("Name:",name)
    print("Runs:",runs)
    print("---------------------------------------------------------------------------------")
#display top 5 bowlers
print("Top 5 Bowlers: ")
bowlers=[]
for player_name,player in players.items():
    bowlers.append((player["wickets"],player_name))#appending the wickets and player name
bowlers.sort(reverse=True)
for wickets,name in bowlers[:5]:#sorting the wickets and player name
    print("Name:",name)
    print("Wickets:",wickets)
print("---------------------------------------------------------------------------------")  
#creating a separate dictionary for award winners
award_winners={}
for player_name,player in players.items():
    if player["runs"]>300 and player["wickets"]>5:
        award_winners[player_name]=player
print("Award Winners: ")
for player_name,player in award_winners.items():
    print("Name:",player_name)
    print("Runs:",player["runs"])
    print("Matches:",player["matches"])
    print("Wickets:",player["wickets"])
print("---------------------------------------------------------------------------------")
