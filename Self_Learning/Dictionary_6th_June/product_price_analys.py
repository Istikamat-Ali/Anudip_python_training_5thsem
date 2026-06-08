'''6. Product Price Analysis
Sample Data
prices = {
 "Laptop": 55000,
 "Mouse": 800,
 "Keyboard": 1800,
 "Monitor": 12000,
 "Printer": 9000,
 "Tablet": 28000,
 "Speaker": 3500,
 "Webcam": 2500,
 "Headphones": 4200,
 "Router": 3200
}
Tasks
• Display products costing more than ₹5000. 
• Count products costing less than ₹3000. 
• Find the most expensive product. 
• Create a list of products priced between ₹2000 and ₹10000. 
• Calculate the total value of all products.'''
print("---------------------------Product Price Analysis---------------------------")
#Given Sample Data
prices = {
 "Laptop": 55000,
 "Mouse": 800,
 "Keyboard": 1800,
 "Monitor": 12000,
 "Printer": 9000,
 "Tablet": 28000,
 "Speaker": 3500,
 "Webcam": 2500,
 "Headphones": 4200,
 "Router": 3200
}
#Task 1: Display Products Costing More Than ₹5000
# --------------------------------------------------
print("Products Costing More Than ₹5000:")
#checking products costing more than 5000
for product, cost in prices.items():
    if cost > 5000:
        print(product)
print("\n--------------------------------------------------------------------------")
#Task 2: Count Products Costing Less Than ₹3000
# --------------------------------------------------
print("Number of Products Costing Less Than ₹3000:")
#count products costing less than 3000
count = 0
for _, cost in prices.items():
    if cost < 3000:
        count += 1
print(count)
print("\n--------------------------------------------------------------------------")
#Task 3: Find the Most Expensive Product
# --------------------------------------------------
print("Most Expensive Product:")
#find most expensive product
expensive_product = max(prices, key=prices.get)#it returns the key of the maximum value
print(expensive_product)
print("\n--------------------------------------------------------------------------")
#Task 4: Create a List of Products Priced Between ₹2000 and ₹10000
# --------------------------------------------------
print("Products Priced Between ₹2000 and ₹10000:")
#creating a list of products priced between 2000 and 10000
price_range_products = [product for product, cost in prices.items() if 2000 <= cost <= 10000]
print(price_range_products)
print("\n--------------------------------------------------------------------------")
#Task 5: Calculate the Total Value of All Products
# --------------------------------------------------
print("Total Value of All Products:")
#calculate total value of all products
total_value = sum(prices.values())
print(total_value)
print("\n--------------------------------------------------------------------------")