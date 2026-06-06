'''Problem Statement
An online store records orders as:
orders = [
 ("Laptop", 55000),
 ("Mouse", 800),
 ("Keyboard", 1500),
 ("Monitor", 12000),
 ("Pen Drive", 600)
]
Write a program to:
• Display all products costing more than ₹1000. 
• Find the most expensive product. 
• Calculate the total order value. 
• Count products costing below ₹1000.'''
print("---------------------------Ecommerce Order Analysis--------------------------")
#Given List containing orders
orders = [
 ("Laptop", 55000),
 ("Mouse", 800),
 ("Keyboard", 1500),
 ("Monitor", 12000),
 ("Pen Drive", 600)
]
#Task 1: Display All Products Costing More Than ₹1000
# --------------------------------------------------
print("Products Costing More Than ₹1000:")
#checking products costing more than 1000
for product, cost in orders:
    if cost > 1000:
        print(product, ":", cost)
print("\n--------------------------------------------------------------------------")
#Task 2: Find The Most Expensive Product
# --------------------------------------------------
print("Most Expensive Product:")
#checking most expensive product
max_cost = orders[0][1]
most_expensive_product = orders[0][0]
for product, cost in orders:
    if cost > max_cost:
        max_cost = cost
        most_expensive_product = product
print(most_expensive_product, ":", max_cost)
print("\n--------------------------------------------------------------------------")
#Task 3: Calculate The Total Order Value
# --------------------------------------------------
print("Total Order Value:")
#calculate total order value
total_order_value = 0
for _, cost in orders:#tuple unpacking for product and cost
    total_order_value += cost
print(total_order_value)
print("\n--------------------------------------------------------------------------")
#Task 4: Count Products Costing Below ₹1000
# --------------------------------------------------
print("Number of Products Costing Below ₹1000:")
#count products costing below 1000
#initialize count
count = 0
for product, cost in orders:
    if cost < 1000:
        count += 1
print(count)
print("\n--------------------------------------------------------------------------")