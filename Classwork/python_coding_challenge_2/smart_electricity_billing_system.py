'''Python Coding Challenge 
Problem 1: Smart Electricity Billing System 
Problem Statement 
Monthly electricity consumption (units) of different houses in a residential society is stored as follows: 
Sample Data 
units = { 
    "House101": 320, 
    "House102": 180, 
    "House103": 510, 
    "House104": 275, 
    "House105": 150, 
    "House106": 430, 
    "House107": 220, 
    "House108": 390, 
    "House109": 145, 
    "House110": 600 
} 
Tasks 
1. Display houses consuming more than 400 units.  
2. Find the highest-consuming house.  
3. Find the lowest-consuming house.  
4. Calculate the total units consumed.  
5. Create separate lists for:  
o Low Consumption (< 200)  
o Medium Consumption (200–400)  
o High Consumption (> 400)  
6. Count houses eligible for an energy-saving campaign (consumption > 300).  
Sample Output 
Houses Consuming More Than 400 Units: 
House103 
House106 
House110 
 
Highest Consumption: 
House110 (600 units) 
 
Lowest Consumption: 
House109 (145 units) 
 
Total Units Consumed: 3220 
 
Low Consumption: 
['House102', 'House105', 'House109'] 
 
Medium Consumption: 
['House101', 'House104', 'House107', 'House108'] 
 
High Consumption: 
['House103', 'House106', 'House110'] 
 
Eligible for Energy-Saving Campaign: 5 '''
#given dictionary of house and unit consumptions
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}
# display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house in units:
    if units[house]>400:
        print(house)
print()
#finding highest consuming houses
for house,consumption in units.items():
    if consumption == max(units.values()):
        print("Highest Consumption:")
        print(house, "(", consumption, "units)")
        break
print()
#finding lowest consuming houses
for house, consumption in units.items():
    if consumption == min(units.values()):
        print("Lowest Consumption:")
        print(house, "(", consumption, "units)")
        break
print()
#total units consumed
total_units = sum(units.values())
print("Total Units Consumed:", total_units)
print()
#creating separate lists for low, medium and high consumption
low_consumption = []
medium_consumption = []
high_consumption = []
for house, consumption in units.items():
    if consumption < 200:
        low_consumption.append(house) #for low consumption should be less than 200
    elif 200 <= consumption <= 400:
        medium_consumption.append(house) # for medium consumption should be between 200 and 400
    else:
        high_consumption.append(house) # for high consumption should be greater than 400
print("Low Consumption:")
print(low_consumption)
print()
print("Medium Consumption:")
print(medium_consumption)
print()
print("High Consumption:")
print(high_consumption)
print()
#counting houses eligible for an energy-saving campaign
campaign_count = 0
for house, consumption in units.items():
    if consumption > 300:
        campaign_count += 1
print("Eligible for Energy-Saving Campaign:", campaign_count)


