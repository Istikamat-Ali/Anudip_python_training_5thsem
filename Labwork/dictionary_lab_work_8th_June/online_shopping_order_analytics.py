'''1. Online Shopping Order Analytics
Problem Statement
An e-commerce company stores product sales data as:
sales = {
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
1. Display products sold more than 20 times. 
2. Find the best-selling product. 
3. Find the least-selling product. 
4. Calculate total products sold. 
5. Create a list of products requiring promotion (sales < 15). 
6. Count products having sales between 10 and 30. 
Sample Output
Products Sold More Than 20 Times:
Mouse
Keyboard
Headphones
Router
Best Selling Product: Mouse (45)
Least Selling Product: Printer (8)
Total Units Sold: 213
Products Requiring Promotion:
['Monitor', 'Printer', 'Tablet']
Products Having Sales Between 10 and 30: 6'''
print("---------------------------Online Shopping Order Analytics---------------------------")
#Given Sample Data
sales = {
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
print("--------------------------------------------------------------------------")
#Task 1: Display Products Sold More Than 20 Times
# --------------------------------------------------
print("Products Sold More Than 20 Times:")
#checking products sold more than 20 times
for product, count in sales.items():
    if count > 20:
        print(product)
print("--------------------------------------------------------------------------")
#Task 2: Find The Best-Selling Product
# --------------------------------------------------
print("Best Selling Product:")
#finding best selling product
best_selling_product = max(sales, key=sales.get)#best selling product is the key of the maximum value
print(best_selling_product, ":", sales[best_selling_product])
print("--------------------------------------------------------------------------")
#Task 3: Find The Least-Selling Product
# --------------------------------------------------
print("Least Selling Product:")
#finding least selling product
least_selling_product = min(sales, key=sales.get)#least selling product is the key of the minimum value
print(least_selling_product, ":", sales[least_selling_product])
print("--------------------------------------------------------------------------")
#Task 4: Calculate Total Units Sold
# --------------------------------------------------
print("Total Units Sold:")
#calculate total units sold
total_units_sold = sum(sales.values())#sum of all values
print(total_units_sold)
print("--------------------------------------------------------------------------")
#Task 5: Create A List Of Products Requiring Promotion
# --------------------------------------------------
print("Products Requiring Promotion:")
#creating a list of products requiring promotion
products_requiring_promotion = [product for product, count in sales.items() if count < 15]#generator expression for products requiring promotion
print(products_requiring_promotion)
print("--------------------------------------------------------------------------")
#Task 6: Count Products Having Sales Between 10 and 30
# --------------------------------------------------
print("Products Having Sales Between 10 and 30:")
#counting products having sales between 10 and 30
count = sum(1 for count in sales.values() if 10 <= count <= 30)#generator expression for count
print(count)
print("--------------------------------------------------------------------------")