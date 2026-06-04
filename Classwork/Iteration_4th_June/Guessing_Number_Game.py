#program to implement guessing number game
#initialize secret number
secret_number=7
#loop until user guesses the correct number
while True:
    #input of user guess
    user_guess=int(input("Guess the Number : "))
    #check if user guess is correct
    if(user_guess==secret_number):
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong Guess. Try Again.")