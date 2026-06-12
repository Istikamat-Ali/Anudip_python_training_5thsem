'''Problem 8: Smart Water Consumption Monitoring System 
Problem Statement 
Monthly water consumption (in litres) of households is recorded below. 
Sample Data 
water_usage = { 
    "House101": 1800, 
    "House102": 2200, 
    "House103": 3500, 
    "House104": 2800, 
    "House105": 1600, 
    "House106": 4100, 
    "House107": 2400, 
    "House108": 3900, 
    "House109": 1500, 
    "House110": 4500 
} 
Tasks 
1. Display houses consuming more than 3000 litres.  
2. Find the highest and lowest consumers.  
3. Calculate total water consumption.  
4. Categorize houses:  
o Low (<2000 litres)  
o Medium (2000–3500 litres)  
o High (>3500 litres)  
5. Count households eligible for conservation awareness programs (>2500 litres).  
Sample Output 
Houses Consuming More Than 3000 Litres: 
House103 
House106 
House108 
House110 
 
Highest Consumption: 
House110 (4500 litres) 
 
Lowest Consumption: 
House109 (1500 litres) 
 
Total Consumption: 28,300 litres 
 
Low Consumption: 
['House101', 'House105', 'House109'] 
 
Medium Consumption: 
['House102', 'House103', 'House104', 'House107'] 
 
High Consumption: 
['House106', 'House108', 'House110'] 
 
Eligible Households: 5 '''
print("---------------------Smart Water Consumption Monitoring System---------------------")
#given list for water consumption
water_usage = {
    "House101": 1800,
    "House102": 2200,
    "House103": 3500,
    "House104": 2800,
    "House105": 1600,
    "House106": 4100,
    "House107": 2400,
    "House108": 3900,
    "House109": 1500,
    "House110": 4500
}
#display houses consuming more than 3000 litres
print("Houses Consuming More Than 3000 Litres: ")
for house in water_usage:
    if water_usage[house]>3000:
        print(house)
print()
#find the highest and lowest consumers
highest_consumer=None #variable to store highest consumer
lowest_consumer=None #variable to store lowest consumer
for house in water_usage:
    if highest_consumer is None or water_usage[house]>water_usage[highest_consumer]:
        highest_consumer=house
    if lowest_consumer is None or water_usage[house]<water_usage[lowest_consumer]:
        lowest_consumer=house
print("Highest Consumption: ")
print(highest_consumer, "(", water_usage[highest_consumer], "litres)")
print()
print("Lowest Consumption: ")
print(lowest_consumer, "(", water_usage[lowest_consumer], "litres)")
print()
#calculate total water consumption
total_consumption = sum(water_usage.values())
print("Total Consumption: ", total_consumption, "litres")
print()
#Categorize houses
low_consumption = []
medium_consumption = []
high_consumption = []
for house in water_usage:
    if water_usage[house] < 2000:
        low_consumption.append(house)
    elif water_usage[house] < 3500:
        medium_consumption.append(house)
    else:
        high_consumption.append(house)
print("Low Consumption: \n", low_consumption)
print()
print("Medium Consumption: \n", medium_consumption)
print()
print("High Consumption: \n", high_consumption)
print()
#Count households eligible for conservation awareness programs
eligible_households = 0
for house in water_usage:
    if water_usage[house] > 2500:
        eligible_households += 1
print("Eligible Households: ", eligible_households)
