'''Problem 5: Online Shopping Cart Analyzer
Problem Statement
The prices of products added to a shopping cart are stored below.
Sample Data
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]
Tasks
1. Calculate the total cart value. 
2. Find the most expensive and cheapest products. 
3. Count products eligible for premium shipping (price > ₹1000). 
4. Generate a discount list (products above ₹1500). 
5. Calculate the average product price. 
Sample Output
Total Cart Value: ₹11,097
Most Expensive Product: ₹2,500
Cheapest Product: ₹300
Premium Shipping Eligible Products: 4
Discount Eligible Products:
[2500, 1800]
Average Product Price: ₹1,109.7'''
#Given list
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]
#calculate total cart value
total_cart_value = sum(cart)
print("Total Cart Value: ₹", total_cart_value)
#find most expensive product
most_expensive_product = max(cart)
print("Most Expensive Product: ₹", most_expensive_product)
#find cheapest product
cheapest_product = min(cart)
print("Cheapest Product: ₹", cheapest_product)
#count products eligible for premium shipping
premium_shipping_count = sum(1 for price in cart if price > 1000) #for premium shopping eligible price>1000
print("Premium Shipping Eligible Products:", premium_shipping_count)
#generate discount list
discount_list = [price for price in cart if price > 1500]# for product above 1500
print("Discount Eligible Products:\n", discount_list)
#calculate average product price
average_product_price = sum(cart) / len(cart)# average product price is sum of all product prices divided by the number of products
print("Average Product Price: ₹", average_product_price)