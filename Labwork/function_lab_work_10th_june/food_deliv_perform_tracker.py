'''2. Food Delivery Performance Tracker 
Problem Statement 
Delivery times (in minutes) for different orders are given below: 
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Requirements 
Create the following functions: 
1. fastest_delivery(times) 
Returns the shortest delivery time. 
2. delayed_orders(times) 
Returns a list of orders taking more than 45 minutes. 
3. average_delivery_time(times) 
Returns the average delivery time. 
4. delivery_category(times) 
Displays order categories: 
• Fast → ≤ 30 minutes  
• Normal → 31–45 minutes  
• Delayed → > 45 minutes  
Sample Output 
Fastest Delivery: 18 minutes 
 
Delayed Orders: 
[60, 80, 55] 
 
Average Delivery Time: 
40.8 minutes 
 
Categories: 
28 -> Fast 
45 -> Normal 
60 -> Delayed 
...'''
print("------------ Food Delivery Performance Tracker ------------")
#input list of delivery times
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]
#function to find the shortest delivery time
def fastest_delivery(times):
    return min(times)

#function to find the orders taking more than 45 minutes
def delayed_orders(times):
    delayed = []
    for time in times:
        if time > 45:
            delayed.append(time)
    return delayed

#function to find the average delivery time
def average_delivery_time(times):
    return sum(times) / len(times)#sum(list) returns the sum of all elements in the list, len(list) returns the number of elements in the list

#function to display order categories
def delivery_category(times):
    for time in times:
        if time <= 30:
            print(f"{time} -> Fast")
        elif time > 30 and time <= 45:
            print(f"{time} -> Normal")
        else:
            print(f"{time} -> Delayed")
print("Fastest Delivery:", fastest_delivery(delivery_time))
print()
print("Delayed Orders:", delayed_orders(delivery_time))
print()
print("Average Delivery Time:", average_delivery_time(delivery_time))
print()
print("Categories:")
delivery_category(delivery_time)