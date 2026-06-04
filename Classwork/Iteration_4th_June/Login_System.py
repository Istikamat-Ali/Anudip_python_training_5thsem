#program to verify user password for login
#initialize valid password
valid_password="admin123"
#loop until user enters the correct password
while True:
    #input of user password
    user_password=input("Enter password : ")
    #check if user password is correct
    if(user_password==valid_password):
        print("Password is correct ... Access granted")
        break
    else:
        print("Invalid password ... Try again")