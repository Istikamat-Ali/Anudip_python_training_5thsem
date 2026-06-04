# program that repeatedly asks the user to enter a PIN until the correct PIN is entered
#initialize valid PIN
valid_pin=1234
#loop until user enters the correct PIN
while True:
    #input of user PIN
    user_pin=int(input("Enter PIN : "))
    #check if user PIN is correct
    if(user_pin==valid_pin):
        print("PIN is correct ... Access granted")
        break
    else:
        print("Incorrect PIN ... Try again")