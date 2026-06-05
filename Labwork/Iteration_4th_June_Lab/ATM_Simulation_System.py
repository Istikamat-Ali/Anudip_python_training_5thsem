#program to simulate an ATM system
print("---------------------ATM Simulation System---------------------")
# initializing balance
balance = 10000 
while True:
    # displaying menu
    print("\nMenu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    # input choice from user
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        # check balance
        print("Your current balance is: ₹", balance)
        
    elif choice == '2':
        # deposit money
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            balance += amount
            print("₹", amount, "deposited successfully. New balance: ₹", balance)
            
    elif choice == '3':
        # withdraw money
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > balance:
            print("Insufficient balance. Your current balance is: ₹", balance)
        else:
            balance -= amount
            print("₹", amount, "withdrawn successfully. New balance: ₹", balance)
            
    elif choice == '4':
        # exit the system
        print("Thank you for using the ATM Simulation System. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please enter a number between 1 and 4.") 
        
