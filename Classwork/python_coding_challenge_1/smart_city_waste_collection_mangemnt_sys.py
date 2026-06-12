'''Problem 10: Smart City Waste Collection Management System 
Problem Statement 
The amount of waste collected (in kilograms) from different sectors of a city is stored below. 
Sample Data 
waste = { 
    "Sector1": 320, 
    "Sector2": 180, 
    "Sector3": 510, 
    "Sector4": 275, 
    "Sector5": 150, 
    "Sector6": 430, 
    "Sector7": 220, 
    "Sector8": 390, 
    "Sector9": 145, 
    "Sector10": 600 
} 
Tasks 
1. Display sectors generating more than 400 kg of waste.  
2. Find the sector generating maximum waste.  
3. Find the sector generating minimum waste.  
4. Calculate the total waste collected.  
5. Categorize sectors:  
o Low Waste (<200 kg)  
o Medium Waste (200–400 kg)  
o High Waste (>400 kg)  
6. Count sectors requiring awareness campaigns (waste generation >300 kg).  
7. Save the awareness campaign list to campaign_sectors.txt.  
Sample Output 
Sectors Generating More Than 400 kg Waste: 
Sector3 
Sector6 
Sector10 
 
Maximum Waste Generation: 
Sector10 (600 kg) 
 
Minimum Waste Generation: 
Sector9 (145 kg) 
 
Total Waste Collected: 3220 kg 
 
Low Waste: 
['Sector2', 'Sector5', 'Sector9'] 
 
Medium Waste: 
['Sector1', 'Sector4', 'Sector7', 'Sector8'] 
 
High Waste: 
['Sector3', 'Sector6', 'Sector10'] 
 
Sectors Requiring Awareness Campaign: 
Sector1 
Sector3 
Sector6 
Sector8 
Sector10 
 
Campaign Report Generated Successfully.'''
print("---Smart City Waste Collection Management System---")
#given dictionary of waste collection data
waste = {
    "Sector1": 320,
    "Sector2": 180,
    "Sector3": 510,
    "Sector4": 275,
    "Sector5": 150,
    "Sector6": 430,
    "Sector7": 220,
    "Sector8": 390,
    "Sector9": 145,
    "Sector10": 600
}
# Task 1: Display sectors generating more than 400 kg of waste
print("Sectors Generating More Than 400 kg Waste:")
for sector, waste_amount in waste.items():
    if waste_amount > 400:
        print(f"{sector}")
print()
# Task 2: Find the sector generating maximum waste
max_waste_sector = None
for sector in waste:
    if max_waste_sector is None or waste[sector] > waste[max_waste_sector]:
        max_waste_sector = sector
print(f"Maximum Waste Generation:\n {max_waste_sector} ({waste[max_waste_sector]} kg)")
print()
# Task 3: Find the sector generating minimum waste
min_waste_sector = None
for sector in waste:
    if min_waste_sector is None or waste[sector] < waste[min_waste_sector]:
        min_waste_sector = sector
print(f"Minimum Waste Generation:\n {min_waste_sector} ({waste[min_waste_sector]} kg)")
print()
# Task 4: Calculate the total waste collected
total_waste = sum(waste.values())
print(f"Total Waste Collected: {total_waste} kg")
print()
# Task 5: Categorize sectors
low_waste = []
medium_waste = []
high_waste = []
for sector, waste_amount in waste.items():
    if waste_amount < 200:
        low_waste.append(sector)
    elif 200 <= waste_amount <= 400:
        medium_waste.append(sector)
    else:
        high_waste.append(sector)
print("Low Waste:")
print(low_waste)
print()
print("Medium Waste:")
print(medium_waste)
print()
print("High Waste:")
print(high_waste)
print()
# Task 6: Count sectors requiring awareness campaigns
print("Sectors Requiring Awareness Campaign:")
for sector, waste_amount in waste.items():
    if waste_amount > 300:
        print(f"{sector}")
print()
# Task 7: Save the awareness campaign list to campaign_sectors.txt
#creating a list of sectors requiring awareness campaigns
campaign_sectors = [sector for sector, waste_amount in waste.items() if waste_amount > 300]
with open("campaign_sectors.txt", "w") as file:
    for sector in campaign_sectors:
        file.write(f"{sector}\n")
print("Campaign Report Generated Successfully.")
