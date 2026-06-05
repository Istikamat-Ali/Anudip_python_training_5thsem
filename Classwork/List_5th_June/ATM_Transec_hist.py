'''Problem Statement
A customer's transactions are stored as:
transactions = [5000, -2000, 3000, -1000, -500, 7000]
Positive values represent deposits and negative values represent withdrawals.
Write a program to:
1. Calculate the current balance. 
2. Count total deposits and withdrawals. 
3. Find the largest deposit and largest withdrawal. 
4. Create separate lists for deposits and withdrawals.'''
# Bank Transaction Analyzer
# List of customer transactions
# Positive values = Deposits
# Negative values = Withdrawals
# Given list
transactions = [5000, -2000, 3000, -1000, -500, 7000]
# --------------------------------------------------
print("----------------------Calculate Current Balance----------------------------")
# --------------------------------------------------
#initialization of current balance
balance = 0
#check the total amounts
for amount in transactions:
    balance += amount #updating the balance
print("Current Balance:", balance)
# --------------------------------------------------
print("-------------------Count Total Deposits and Withdrawals---------------------")
# --------------------------------------------------
#initialize diposits and withdrawals count variables
deposit_count = 0
withdrawal_count = 0
#checking deposits and withdrawal counts
for amount in transactions:
    if amount > 0: #for diposit
        deposit_count += 1
    elif amount < 0:#for withdrawals
        withdrawal_count += 1

print("Total Deposits:", deposit_count)
print("Total Withdrawals:", withdrawal_count)

# --------------------------------------------------
print("---------------Find Largest Deposit and Largest Withdrawal-----------------")
# --------------------------------------------------
# Initialize variables to find largest diposits and withdrawals
#check largest diposit and withdrawals
largest_deposit = 0
largest_withdrawal = 0
#check largest diposit and withdrawals
for amount in transactions:
    #for largest diposit amount
    if amount > 0:
        if amount > largest_deposit:
            largest_deposit = amount
    #for largest withdrawal amount
    else:
        if abs(amount) > abs(largest_withdrawal):
            largest_withdrawal = amount

print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)

# --------------------------------------------------
print("------------Create Separate Lists for Deposits and Withdrawals-------------")
# --------------------------------------------------
#initialize an empty list for deposits and withdrawals
deposits = []
withdrawals = []
#making the separate lists for both
for amount in transactions:
    if amount > 0:#for deposit amount
        deposits.append(amount)
    elif amount < 0:#for withdrawal amount
        withdrawals.append(amount)

print("Deposits List:", deposits)
print("Withdrawals List:", withdrawals)