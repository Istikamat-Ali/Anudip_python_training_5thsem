''' Inventory Management System
Sample Data
inventory = {
 "Notebook": 45,
 "Pen": 120,
 "Pencil": 80,
 "Eraser": 25,
 "Marker": 15,
 "Stapler": 8,
 "Glue": 12,
 "Scale": 30,
 "Folder": 5,
 "Calculator": 3
}
Tasks
• Display products with stock less than 10. 
• Count products having stock more than 50. 
• Find the product with the minimum stock. 
• Create a list of products that require restocking (stock < 20). 
• Calculate the total inventory count.'''
# Given Sample Data
inventory = {
 "Notebook": 45,
 "Pen": 120,
 "Pencil": 80,
 "Eraser": 25,
 "Marker": 15,
 "Stapler": 8,
 "Glue": 12,
 "Scale": 30,
 "Folder": 5,
 "Calculator": 3
}
# --------------------------------------------------
print("--------------------Display Products That Are Out of Stock-----------------")
# --------------------------------------------------
print("Products Out of Stock:")
#checking products in stocks
for product, quantity in inventory.items():
    if quantity == 0:#for out of stock product
        print(product, end=" ")
print("\n--------------------------------------------------------------------------")
# --------------------------------------------------
print("---------------------Display Products That Need Restocking--------------------")
# ------------------------------------------------
#Quantity less than 20 but greater than 0
print("Products Needing Restocking:")
#checking products need to be restocked
for product, quantity in inventory.items():
    if quantity < 20 and quantity > 0:
        print(product, end=" ")
print("\n--------------------------------------------------------------------------")
# --------------------------------------------------
print("----------------------------Count Available Products-------------------------")
# --------------------------------------------------
#Products having stock greater than 0
#initialize available products variable to 0
available_products = 0
#check available products ,count greater than zero
for quantity in inventory.values():
    if quantity > 0:#for available products
        available_products += 1
print("Number of Available Products:", available_products)
print("\n-----------------------------------------------------------------------------")
# --------------------------------------------------
print("--------------------------Create a New List of Products----------------------- ")
# --------------------------------------------------
# Having Stock Greater Than or Equal to 50
#initialize stocked product to zero
high_stock_products = []
#checking for stock product greater than  or equal to 50
for quantity in inventory.values():
    if quantity >= 50:
        high_stock_products.append(quantity)
print("Products with Stock >= 50:", high_stock_products)
print("\n----------------------------------------------------------------------------------")
# --------------------------------------------------
print("--------------------------Find the Product with Minimum Stock----------------------- ")
# --------------------------------------------------
#finding the product with minimum stock
minimum_stock_product = min(inventory, key=inventory.get)
print("Product with Minimum Stock:", minimum_stock_product)
print("\n----------------------------------------------------------------------------------")
# --------------------------------------------------
print("--------------------------Calculate the Total Inventory Count----------------------- ")
# --------------------------------------------------
#calculate total inventory count
total_inventory_count = sum(inventory.values())
print("Total Inventory Count:", total_inventory_count)
print("\n----------------------------------------------------------------------------------")

