'''Problem 3: Smart Parking Management System
Problem Statement
The parking status of vehicles in a mall is maintained as follows.
Sample Data
parking_slots = [
 "Occupied", "Vacant", "Occupied", "Vacant",
 "Occupied", "Occupied", "Vacant", "Occupied",
 "Vacant", "Occupied"
]
Tasks
1. Display vacant parking slot numbers. 
2. Count occupied and vacant slots. 
3. Allocate the first vacant slot to a new vehicle. 
4. Calculate parking occupancy percentage. 
5. Store updated parking information in parking.txt. 
Sample Output
Vacant Parking Slots:
2 4 7 9
Occupied Slots: 6
Vacant Slots: 4
Vehicle Allocated to Slot 2
Occupancy Percentage: 70.0%
Parking Details Saved Successfully'''
#given list of parking slots
parking_slots = [
 "Occupied", "Vacant", "Occupied", "Vacant",
 "Occupied", "Occupied", "Vacant", "Occupied",
 "Vacant", "Occupied"
]
#display vacant parking slots 
print("Vacant Parking Slots:")
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        print(i + 1, end=" ")# as slot no starts from 1 and index starts from 0
print()
#count occupied and vacant slots
occupied_slots = 0
vacant_slots = 0
for slot in parking_slots:
    if slot == "Occupied":
        occupied_slots += 1
    else:
        vacant_slots += 1
print("Occupied Slots:", occupied_slots)
print("Vacant Slots:", vacant_slots)
#allocate the first vacant slot to a new vehicle
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        parking_slots[i] = "Occupied"
        print("Vehicle Allocated to Slot", i + 1)
        break
#calculate parking occupancy percentage
total_slots = len(parking_slots)
occupancy_percentage = (total_slots - vacant_slots) / total_slots * 100
print("Occupancy Percentage:", round(occupancy_percentage,1),"%")
#store updated parking information in parking.txt
with open("parking.txt", "w") as file:
    for slot in parking_slots:
        file.write(slot + "\n")
print("Parking Details Saved Successfully")