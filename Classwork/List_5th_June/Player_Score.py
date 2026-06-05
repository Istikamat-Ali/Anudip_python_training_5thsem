# Program to input scores of 11 players
# and display all scores at the end
# Without using list

print("--------------------- Player Score Management System ---------------------")

# Input scores for all 11 players

p1 = float(input("Enter score for Player 1: "))
# validate input
if p1 < 0:
    exit("Score cannot be negative ... Exited")

p2 = float(input("Enter score for Player 2: "))
# validate input
if p2 < 0:
    exit("Score cannot be negative ... Exited")

p3 = float(input("Enter score for Player 3: "))
# validate input
if p3 < 0:
    exit("Score cannot be negative ... Exited")

p4 = float(input("Enter score for Player 4: "))
# validate input
if p4 < 0:
    exit("Score cannot be negative ... Exited")

p5 = float(input("Enter score for Player 5: "))
# validate input
if p5 < 0:
    exit("Score cannot be negative ... Exited")

p6 = float(input("Enter score for Player 6: "))
# validate input
if p6 < 0:
    exit("Score cannot be negative ... Exited")

p7 = float(input("Enter score for Player 7: "))
# validate input
if p7 < 0:
    exit("Score cannot be negative ... Exited")

p8 = float(input("Enter score for Player 8: "))
# validate input
if p8 < 0:
    exit("Score cannot be negative ... Exited")

p9 = float(input("Enter score for Player 9: "))
# validate input
if p9 < 0:
    exit("Score cannot be negative ... Exited")

p10 = float(input("Enter score for Player 10: "))
# validate input
if p10 < 0:
    exit("Score cannot be negative ... Exited")

p11 = float(input("Enter score for Player 11: "))
# validate input
if p11 < 0:
    exit("Score cannot be negative ... Exited")

# Display all player scores
print("\n--------------------- Player Scores ---------------------")

print("Player 1  Score :", p1)
print("Player 2  Score :", p2)
print("Player 3  Score :", p3)
print("Player 4  Score :", p4)
print("Player 5  Score :", p5)
print("Player 6  Score :", p6)
print("Player 7  Score :", p7)
print("Player 8  Score :", p8)
print("Player 9  Score :", p9)
print("Player 10 Score :", p10)
print("Player 11 Score :", p11)

# display highest score among all players
highest_score = max(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)
print("\nHighest Score :", highest_score)

# display lowest score among all players
lowest_score = min(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)
print("Lowest Score :", lowest_score)

# calculate total score of all players
total_score = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11
print("Total Score :", total_score)

# calculate average score of all players
average_score = total_score / 11
print("Average Score :", average_score)

