'''Problem Statement
An inventory manager stores stock quantities as:
stock = [25, 5, 0, 12, 3, 18, 0, 30]
Write a program to:
1. Display products that are out of stock. 
2. Display products that need restocking (quantity less than 10). 
3. Count available products. 
4. Create a new list containing only products with stock greater than or equal to 15.'''
print("-------------------------Inventory Management System----------------------")
#Given List containing stock quantities of products
stock = [25, 5, 0, 12, 3, 18, 0, 30]
# --------------------------------------------------
print("--------------------Display Products That Are Out of Stock-----------------")
# --------------------------------------------------
print("Products Out of Stock:")
#checking products in stocks
for quantity in stock:
    if quantity == 0:#for out of stock product
        print(quantity, end=" ")
print("\n--------------------------------------------------------------------------")
# --------------------------------------------------
print("---------------------Display Products That Need Restocking--------------------")
# ------------------------------------------------
#Quantity less than 10 but greater than 0
print("Products Needing Restocking:")
#checking products need to be restocked
for quantity in stock:
    if quantity < 10 and quantity > 0:
        print(quantity, end=" ")
print("\n--------------------------------------------------------------------------")
# --------------------------------------------------
print("----------------------------Count Available Products-------------------------")
# --------------------------------------------------
#Products having stock greater than 0
#initialize available products variable to 0
available_products = 0
#check available products ,count greater than zero
for quantity in stock:
    if quantity > 0:#for available products
        available_products += 1
print("Number of Available Products:", available_products)
print("\n-----------------------------------------------------------------------------")
# --------------------------------------------------
print("--------------------------Create a New List of Products----------------------- ")
# --------------------------------------------------
# Having Stock Greater Than or Equal to 15
#initialize stocked product to zero
high_stock_products = []
#checking for stock product greater than  or equal to 15
for quantity in stock:
    if quantity >= 15:
        high_stock_products.append(quantity)
print("Products with Stock >= 15:", high_stock_products)