#program to calculate electricity bill based on slab rates
print("---------------------Electricity Bill Calculator---------------------")
# input units consumed from user
units_consumed = float(input("Enter the number of units consumed: "))
# validating the input
if units_consumed < 0:
    exit("Units consumed cannot be negative ...Exited")
print("-------------------------------------------------------------")
# initializing total bill
total_bill = 0
# calculating total bill based on slab rates
if units_consumed <= 100:
    total_bill = units_consumed * 5
    category = "Low Consumption"
elif units_consumed <= 200:
    total_bill = (100 * 5) + ((units_consumed - 100) * 7)
    category = "Medium Consumption"
else:
    total_bill = (100 * 5) + (100 * 7) + ((units_consumed - 200) * 10)
    category = "High Consumption"
# displaying the result
print("Units Consumed:", units_consumed)
print("Total Bill: ₹", total_bill)
print("Category:", category)      
