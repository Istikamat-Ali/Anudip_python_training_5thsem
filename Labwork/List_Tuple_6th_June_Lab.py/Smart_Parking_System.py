'''3. Smart Parking System
Problem Statement
Parking slots are represented as:
slots = [1, 0, 1, 1, 0, 0, 1, 0]
Where:
• 1 = Occupied 
• 0 = Available 
Write a program to:
• Count occupied and available slots. 
• Find the first available slot. 
• Display all available slot numbers. 
• Check whether parking occupancy exceeds 75%.'''
print("---------------------- Smart Parking System ----------------------")
#Given list of slots
slots = [1, 0, 1, 1, 0, 0, 1, 0] #1=occupied, 0=available
#Count occupied and available slots
occupied_slots = slots.count(1)#counting occupied slots count(value)
available_slots = slots.count(0)#counting available slots count(value)
print("Occupied Slots:",occupied_slots)
print("Available Slots:",available_slots)
print("------------------------------------------------------------------------")
#Find the first available slot
for i in range(len(slots)):
    if slots[i] == 0:
        print("First Available Slot Number:",i+1)#as slot no starts from 1 and index starts from 0
        break #breaking the loop
print("------------------------------------------------------------------------")
#Display all available slot numbers
#creating an empty list for available slot numbers
available_slot_numbers = []
#finding all available slot numbers
for i in range(len(slots)):
    if slots[i] == 0:
        available_slot_numbers.append(i+1) #push the available slot numbers at the end of the list
print("Available Slot Numbers:",available_slot_numbers)
print("------------------------------------------------------------------------")
#Check whether parking occupancy exceeds 75%
occupied_slots = slots.count(1)
if occupied_slots/len(slots)*100 > 75: #occupancy_percentage = (occupied_slots / total_slots) * 100
    print("Parking Occupancy Exceeds 75%")
else:
    print("Parking Occupancy Does Not Exceed 75%")
print("------------------------------------------------------------------------")
