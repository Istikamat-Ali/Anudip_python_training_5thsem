'''Problem 3: Food Delivery Performance Dashboard 
Problem Statement 
Delivery times (in minutes) for different orders are recorded below: 
Sample Data 
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Tasks 
1. Find the fastest delivery time.  
2. Find the slowest delivery time.  
3. Calculate the average delivery time.  
4. Display delayed orders (>45 minutes).  
5. Categorize deliveries:  
o Fast (≤30 minutes)  
o Normal (31–45 minutes)  
o Delayed (>45 minutes)  
Sample Output 
Fastest Delivery: 18 minutes 
 
Slowest Delivery: 80 minutes 
 
Average Delivery Time: 40.8 minutes 
 
Delayed Orders: 
[60, 80, 55] 
 
Fast Deliveries: 4 
Normal Deliveries: 3 
Delayed Deliveries: 3 '''
#given data  time in minutes in list
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]
#finding the fastest delivery time 
def find_fastest_delivery(delivery_times):
    return min(delivery_times)
#finding the slowest delivery time 
def find_slowest_delivery(delivery_times):
    return max(delivery_times)
#finding the average delivery time 
def calculate_average_delivery_time(delivery_times):
    return sum(delivery_times) / len(delivery_times)
#finding the delayed orders 
def find_delayed_orders(delivery_times):
    delayed_orders = []
    for time in delivery_times:
        if time > 45:
            delayed_orders.append(time)
    return delayed_orders
#categorizing deliveries  
def categorize_deliveries(delivery_times):
    fast_deliveries = 0
    normal_deliveries = 0
    delayed_deliveries = 0
    for time in delivery_times:
        if time <= 30:
            fast_deliveries += 1
        elif time <= 45:
            normal_deliveries += 1
        else:
            delayed_deliveries += 1
    return fast_deliveries, normal_deliveries, delayed_deliveries
#calling functions
print("Fastest Delivery:", find_fastest_delivery(delivery_times))
print()
print("Slowest Delivery:", find_slowest_delivery(delivery_times))
print()
print("Average Delivery Time:", calculate_average_delivery_time(delivery_times))
print()
print("Delayed Orders:")
print(find_delayed_orders(delivery_times))
print()
print("Fast Deliveries:", categorize_deliveries(delivery_times)[0]) #returning tuple values at index 0
print("Normal Deliveries:", categorize_deliveries(delivery_times)[1]) #returning tuple values at index 1
print("Delayed Deliveries:", categorize_deliveries(delivery_times)[2]) # returning tuple values at index 2
            
            
            
            