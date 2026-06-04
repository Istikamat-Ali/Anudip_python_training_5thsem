# Generate a secret number between 1 and 50.
# Allow the user to keep guessing until the correct number is found.
# Display:
# • "Too High" 
# • "Too Low" 
# • "Correct Guess" 
# Also display the total number of attempts.
#program to implement a number guessing game
print("---------------------Number Guessing Game---------------------")
#initialize the secret number
secret_number = 25
#initialize attempts counter
attempts = 0
while True:
    #input a guess from user
    guess = int(input("Enter your guess (between 1 and 50): "))
    attempts += 1

    if guess < secret_number:
        print("Too Low! Try again.")
    elif guess > secret_number:
        print("Too High! Try again.")
    else:
        print("Correct Guess! The secret number was", secret_number)
        print("Total attempts:", attempts)
        break