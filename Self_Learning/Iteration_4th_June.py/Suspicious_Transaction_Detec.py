#9.> program to detect suspicious transactions based on given criteria
print("---------------------Suspicious Transaction Detector---------------------")
# initializing counters and total amount
above_50000_count = 0
below_1000_count = 0
total_amount = 0
# continuously input transaction amounts until -1 is entered
while True:
    transaction_amount = float(input("Enter transaction amount (or -1 to stop): "))
    if transaction_amount == -1: # check if the user wants to stop entering transactions
        break
    if transaction_amount < 0: # validating the input
        print("Please enter a positive transaction amount...Try again")
        continue
    total_amount += transaction_amount # adding the transaction amount to total
    if transaction_amount > 50000: # checking if the transaction is above ₹50,000
        above_50000_count += 1 # incrementing the counter for transactions above ₹50,000
    elif transaction_amount < 1000: # checking if the transaction is below ₹1,000
        below_1000_count += 1 # incrementing the counter for transactions below ₹1,000
# displaying the results
print("Total transaction amount: ₹", total_amount)
print("Number of transactions above ₹50,000:", above_50000_count)
print("Number of transactions below ₹1,000:", below_1000_count) 