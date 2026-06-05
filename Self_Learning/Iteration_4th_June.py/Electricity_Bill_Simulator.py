# 4.> program to calculate electricity bill
print("---------------------Electricity Bill Simulator---------------------")
# input number of units consumed from user
units = int(input("Enter the number of units consumed: "))
# validating the input
if units < 0:
    exit("Please enter a positive number for units consumed...Exited")
print("-------------------------------------------------------------")
# calculating bill amount based on slabs using if-elif-else statements
if units <= 100:
    bill_amount = units * 5# calculating bill amount for first 100 units
elif units <= 200:
    bill_amount = (100 * 5) + ((units - 100) * 7)# calculating bill amount for first 100 units and remaining units respectively
else:
    bill_amount = (100 * 5) + (100 * 7) + ((units - 200) * 10)# calculating bill amount for first 100 units, next 100 units and remaining units respectively
# adding surcharge if bill amount exceeds ₹5000
if bill_amount > 5000:
    bill_amount += bill_amount * 0.10 # adding 10% surcharge
# displaying the final payable amount
print("Final Payable Amount: ₹", bill_amount)   