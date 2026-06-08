'''10. Electricity Consumption Report
Sample Data
units = {
 "House101": 320,
 "House102": 180,
 "House103": 450,
 "House104": 290,
 "House105": 150,
 "House106": 510,
 "House107": 220,
 "House108": 390,
 "House109": 170,
 "House110": 260
}
Tasks
• Display houses consuming more than 300 units. 
• Count houses consuming less than 200 units. 
• Find the house with the highest consumption. 
• Create a list of houses eligible for an energy-saving awareness campaign (consumption > 400 units). 
• Categorize houses as: 
o Low: < 200 units 
o Medium: 200–350 units 
o High: '''
print("--------------------------Electricity Consumption Report-----------------------------")
#given dictionary
units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}
print("-------------------------------------------------------------")
#displaying houses consuming more than 300 units
print("Houses consuming more than 300 units:")
for house, consumption in units.items():
    if consumption > 300:
        print(house)
print("-------------------------------------------------------------")
#counting houses consuming less than 200 units
print("Number of Houses consuming less than 200 units:")
count = 0
for consumption in units.values():
    if consumption < 200:
        count += 1
print("Number of Houses consuming less than 200 units:", count)
print("-------------------------------------------------------------")
#finding the house with the highest consumption
print("House with highest consumption:")
highest_consumption = max(units.values())
for house, consumption in units.items():
    if consumption == highest_consumption:
        print("House with highest consumption:", house)
        break
print("-------------------------------------------------------------")
#creating a list of houses eligible for an energy-saving awareness campaign
print("Houses eligible for an energy-saving awareness campaign:")
eligible_houses = []
for house, consumption in units.items():
    if consumption > 400:
        eligible_houses.append(house)
print("Houses eligible for an energy-saving awareness campaign:", eligible_houses)
print("-------------------------------------------------------------")
# categorizing houses as low, medium, high
print("Categorizing houses as low, medium, high:")
for house, consumption in units.items():
    if consumption < 200:
        category = "Low"
    elif consumption <= 350:
        category = "Medium"
    else:
        category = "High"
    print("House:", house, "Category:", category)
print("-------------------------------------------------------------")