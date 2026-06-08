'''2. E-Commerce Inventory & Sales Dashboard
Problem Statement
An online store wants to manage products and sales.
Example Structure
products = {
 "P101": {
 "name": "Laptop",
 "price": 55000,
 "stock": 12,
 "sold": 25
 }
}
Maintain records of at least 30 products.
Requirements
1. Display all products. 
2. Add a new product. 
3. Update stock after sales. 
4. Find out-of-stock products. 
5. Find products with stock less than 5. 
6. Calculate total inventory value. 
7. Find best-selling product. 
8. Find least-selling product. 
9. Calculate total revenue generated. 
10. Generate a low-stock report. 
11. Display products whose sales exceed the average sales. 
12. Create a dictionary of products eligible for promotion (sales < 10). 
Challenge
Generate a complete business report.'''
print("------- E-Commerce Inventory & Sales Dashboard -------")
# taking input from user in this format
'''products = {
 "P101": {
 "name": "Laptop",
 "price": 55000,
 "stock": 12,
 "sold": 25
 }
}'''
products = {}
for i in range(10):
    product_id = input("Enter Product ID: ")
    product_name = input("Enter Product Name: ")
    product_price = float(input("Enter Product Price: "))
    product_stock = int(input("Enter Product Stock: "))
    product_sold = int(input("Enter Product Sold: "))
    products[product_id] = {
        "name": product_name,
        "price": product_price,
        "stock": product_stock,
        "sold": product_sold
    }
print("--------------------------------------------------------------------------")
#Task 1: Display All Products
# --------------------------------------------------
print("All Products:")
#displaying all products
for product, details in products.items():
    print(f"Product ID: {product}")#string formating is used to print the values
    print(f"Name: {details['name']}")
    print(f"Price: {details['price']}")
    print(f"Stock: {details['stock']}")
    print(f"Sold: {details['sold']}")
print("--------------------------------------------------------------------------")
#Task 2: Add a New Product
# --------------------------------------------------
print("Add a New Product:")
#add a new product
product_id = input("Enter Product ID: ")
product_name = input("Enter Product Name: ")
product_price = float(input("Enter Product Price: "))
product_stock = int(input("Enter Product Stock: "))
product_sold = int(input("Enter Product Sold: "))
products[product_id] = {
 "name": product_name,
 "price": product_price,
 "stock": product_stock,
 "sold": product_sold
}
print("Product added successfully!")
print("--------------------------------------------------------------------------")
#Task 3: Update Stock After Sales
# --------------------------------------------------
print("Update Stock After Sales:")
#update stock after sales
product_id = input("Enter Product ID: ")
if product_id in products:
    sold_quantity = int(input("Enter Sold Quantity: "))
    products[product_id]["stock"] -= sold_quantity
    products[product_id]["sold"] += sold_quantity
    print("Stock updated successfully!")
else:
    print("Product not found!")
print("--------------------------------------------------------------------------")
#Task 4: Find Out-of-Stock Products
# --------------------------------------------------
print("Out-of-Stock Products:")
#out of stock products
for product, details in products.items():
    if details["stock"] == 0:
        print(f"Product ID: {product}")
        print(f"Name: {details['name']}")
        print(f"Price: {details['price']}")
        print(f"Stock: {details['stock']}")
        print(f"Sold: {details['sold']}")
print("--------------------------------------------------------------------------")
#Task 5: Find Products with Stock Less than 5
# --------------------------------------------------
print("Products with Stock Less than 5:")
#products with stock less than 5
for product, details in products.items():
    if details["stock"] < 5:
        print(f"Product ID: {product}")
        print(f"Name: {details['name']}")
        print(f"Price: {details['price']}")
        print(f"Stock: {details['stock']}")
        print(f"Sold: {details['sold']}")
print("--------------------------------------------------------------------------")
#Task 6: Calculate Total Inventory Value
# --------------------------------------------------
print("Total Inventory Value:")
#total inventory value
total_value = 0
for product, details in products.items():
    total_value += details["price"] * details["stock"]#for calculating total value
print(f"Total Value: {total_value}")
print("--------------------------------------------------------------------------")
#Task 7: Find Best-Selling Product
# --------------------------------------------------
print("Best-Selling Product:")
#best selling product
best_selling_product = max(products, key=lambda product: products[product]["sold"])#for finding best selling product using lambda expression
print(f"Product ID: {best_selling_product}")
print(f"Name: {products[best_selling_product]['name']}")
print(f"Price: {products[best_selling_product]['price']}")
print(f"Stock: {products[best_selling_product]['stock']}")
print(f"Sold: {products[best_selling_product]['sold']}")
print("--------------------------------------------------------------------------")
#Task 8: Find Least-Selling Product
# --------------------------------------------------
print("Least-Selling Product:")
#least selling product
least_selling_product = min(products, key=lambda product: products[product]["sold"])
print(f"Product ID: {least_selling_product}")
print(f"Name: {products[least_selling_product]['name']}")
print(f"Price: {products[least_selling_product]['price']}")
print(f"Stock: {products[least_selling_product]['stock']}")
print(f"Sold: {products[least_selling_product]['sold']}")
print("--------------------------------------------------------------------------")
#Task 9: Calculate Total Revenue Generated
# --------------------------------------------------
print("Total Revenue Generated:")
#total revenue generated
total_revenue = 0
for product, details in products.items():
    total_revenue += details["price"] * details["sold"]
print(f"Total Revenue: {total_revenue}")
print("--------------------------------------------------------------------------")
#Task 10: Generate a Low-Stock Report
# --------------------------------------------------
print("Low-Stock Report:")
#low stock report
for product, details in products.items():
    if details["stock"] < 5:
        print(f"Product ID: {product}")
        print(f"Name: {details['name']}")
        print(f"Price: {details['price']}")
        print(f"Stock: {details['stock']}")
        print(f"Sold: {details['sold']}")
print("--------------------------------------------------------------------------")
#Task 11: Display Products with Sales Exceeding the Average Sales
# --------------------------------------------------
print("Products with Sales Exceeding the Average Sales:")
#products with sales exceeding the average sales
average_sales = sum(details["sold"] for details in products.values()) / len(products)
for product, details in products.items():
    if details["sold"] > average_sales:
        print(f"Product ID: {product}")
        print(f"Name: {details['name']}")
        print(f"Price: {details['price']}")
        print(f"Stock: {details['stock']}")
        print(f"Sold: {details['sold']}")
print("--------------------------------------------------------------------------")
#Task 12: Create a Dictionary of Products Eligible for Promotion
# --------------------------------------------------
print("Products Eligible for Promotion:")
#products eligible for promotion
promotion_products = {}
for product, details in products.items():
    if details["sold"] < 10:
        promotion_products[product] = details
print("Promotion Products:")
for product, details in promotion_products.items():
    print(f"Product ID: {product}")
    print(f"Name: {details['name']}")
    print(f"Price: {details['price']}")
    print(f"Stock: {details['stock']}")
    print(f"Sold: {details['sold']}")
print("--------------------------------------------------------------------------")