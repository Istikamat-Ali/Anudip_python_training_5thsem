'''4. Vehicle Number Plate Verification
Problem Statement
A vehicle number plate is entered:
MH12AB4589
Tasks
Write a program to:
1. Extract state code. 
2. Extract district code. 
3. Extract vehicle series. 
4. Extract vehicle number. 
5. Count letters and digits separately. 
6. Verify: 
o First 2 characters must be alphabets. 
o Next 2 must be digits. 
o Next 2 must be alphabets. 
o Last 4 must be digits. 
7. Display whether the number plate is valid. 
Sample Output
Vehicle Number: MH12AB4589
State Code: MH
District Code: 12
Series: AB
Vehicle Number: 4589
Total Letters: 4
Total Digits: 6
Vehicle Number Status: Valid'''
print("---------------------Vehicle Number Plate Verification---------------------")
#vehicle number plate from user is entered
vehicle_number_plate = "MH12AB4589"
print("-------------------------------------------------------------")
# extract state code
state_code = vehicle_number_plate[:2]
print("State Code:", state_code)
print("-------------------------------------------------------------")
# extract district code
district_code = vehicle_number_plate[2:4]
print("District Code:", district_code)
print("-------------------------------------------------------------")
# extract vehicle series
vehicle_series = vehicle_number_plate[4:6]
print("Vehicle Series:", vehicle_series)
print("-------------------------------------------------------------")
# extract vehicle number
vehicle_number = vehicle_number_plate[6:]
print("Vehicle Number:", vehicle_number)
print("-------------------------------------------------------------")
# count letters and digits separately
letters = 0
digits = 0
for char in vehicle_number_plate:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
print("Total Letters:", letters)
print("Total Digits:", digits)
print("-------------------------------------------------------------")
# verify number plate
if state_code.isalpha() and district_code.isdigit() and vehicle_series.isalpha() and vehicle_number.isdigit():
    print("Vehicle Number Status: Valid")
else:
    print("Vehicle Number Status: Invalid")
