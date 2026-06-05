#program to input 11 players score and display their score
#player score
player_score=[]
#input of score from user
for i in range(11):
    score=int(input("Enter the score of player " + str(i+1) + ": "))
    #validate score 
    if score<0:
        exit("Score cannot be negative ...Exited")
        continue 
    player_score.append(score)
#display the players score 
print("\n-------Player Scores---------")
print("Score of 11 players:",player_score)
#finding the highest score
max_score=player_score[0]
for i in range(1,len(player_score)):
    if player_score[i] > max_score:
        max_score=player_score[i]
print("The highest score is:",max_score)