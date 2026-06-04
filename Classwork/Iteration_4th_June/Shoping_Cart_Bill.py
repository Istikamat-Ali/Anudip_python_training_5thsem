#program to calculate total bill amount for items added to shopping cart
#initialize total bill amount
total_bill=0
#loop until user enters 0
while True:
    #input of item price
    item_price=float(input("Enter item price (0 to stop) : "))
    #validating item price
    if(item_price<0):
        print("Invalid item price ... Try again")
        continue
    elif(item_price==0):
        break
    else:
        total_bill+=item_price
#display total bill amount
print("Total bill amount for items in shopping cart : ", total_bill)