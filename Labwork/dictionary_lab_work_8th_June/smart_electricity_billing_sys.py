'''5. Smart Electricity Billing System
Problem Statement
Monthly electricity consumption (units) is stored as:
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
4. Calculate total units consumed. 
5. Create lists: 
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
Eligible for Energy-Saving Campaign: 5'''
print("---------------------Smart Electricity Billing System---------------------")
#given dictionary
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
# displaying houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house, consumption in units.items():
    if consumption > 400:
        print(house)
print("-------------------------------------------------------------")
# finding the highest-consuming house
print("Highest Consumption:")
highest_consumption = max(units.values())
for house, consumption in units.items():    
    if consumption == highest_consumption:
        print(house, "(", consumption, "units)")
        break
print("-------------------------------------------------------------")
# finding the lowest-consuming house
print("Lowest Consumption:")
lowest_consumption = min(units.values())
for house, consumption in units.items():
    if consumption == lowest_consumption:
        print(house, "(", consumption, "units)")
        break
print("-------------------------------------------------------------")
# calculate total units consumed
print("Total Units Consumed:", sum(units.values()))
print("-------------------------------------------------------------")
# create lists for low, medium, and high consumption
#generator expression for low, medium and high consumption
low_consumption = [house for house, consumption in units.items() if consumption < 200]
medium_consumption = [house for house, consumption in units.items() if 200 <= consumption <= 400]
high_consumption = [house for house, consumption in units.items() if consumption > 400]
print("Low Consumption:", low_consumption)
print("Medium Consumption:", medium_consumption)
print("High Consumption:", high_consumption)
print("-------------------------------------------------------------")
# count houses eligible for an energy-saving campaign
print("Eligible for Energy-Saving Campaign:", len([house for house, consumption in units.items() if consumption > 300]))
print("-------------------------------------------------------------")
