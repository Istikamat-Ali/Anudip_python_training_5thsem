'''Problem 4: Online Shopping Inventory System 
Problem Statement 
An online store maintains stock quantities of products. 
Sample Data 
inventory = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 
Tasks 
1. Display products with stock below 15 units.  
2. Find the product with maximum stock.  
3. Find the product with minimum stock.  
4. Calculate total stock available.  
5. Create a list of products requiring restocking (<10 units).  
Sample Output 
Products with Stock Below 15: 
Monitor 
Printer 
Tablet 
 
Highest Stock Product: 
Mouse (45 units) 
 
Lowest Stock Product: 
Printer (8 units) 
 
Total Stock Available: 213 
 
Products Requiring Restocking: 
['Printer'] '''
# Given Sample Data
inventory = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}
# Display products with stock below 15 units
print("Products with Stock Below 15:")
for product, stock in inventory.items():
    if stock < 15:
        print(product)
print()
# Find the product with maximum stock
print("Highest Stock Product:")
highest_stock = max(inventory.values())
for product, stock in inventory.items():
    if stock == highest_stock:
        print(f"{product} ({stock} units)")
print()
# Find the product with minimum stock
print("Lowest Stock Product:")
lowest_stock = min(inventory.values())
for product, stock in inventory.items():
    if stock == lowest_stock:
        print(f"{product} ({stock} units)")
print()
# Calculate total stock available
print("Total Stock Available:", sum(inventory.values()))
print()
# Create a list of products requiring restocking
print("Products Requiring Restocking:")
restocking_products = [product for product, stock in inventory.items() if stock < 10]#list comprehension is used to create a list
print(restocking_products)

