'''Assignment 4: Vehicle Registration Verification System 
Problem Statement 
A transport department wants to verify vehicle registration numbers. 
Store at least 20 vehicle numbers. 
Example 
MH12AB4589 
DL05XY9988 
KA03PQ1234 
Requirements 
For each registration number: 
1. Extract state code.  
2. Extract district code.  
3. Extract series.  
4. Extract vehicle number.  
5. Count letters and digits.  
6. Validate format:  
o First 2 characters = Alphabets  
o Next 2 characters = Digits  
o Next 2 characters = Alphabets  
o Last 4 characters = Digits  
7. Display invalid registrations.  
8. Count vehicles state-wise.  
Challenge 
Generate a state-wise report: 
MH -> 6 Vehicles 
DL -> 4 Vehicles 
KA -> 5 Vehicles 
UP -> 5 Vehicles'''
print("--------------------------Vehicle Registration Verification System--------------------------")
#creating empty list to store vehicle registration numbers
regis_num=[]
#taking input for vehicle registration numbers
while len(regis_num)<3:
    regis_num.append(input("Enter vehicle registration number: ").strip())
#creating empty dictionary to store state-wise vehicle count
state_count={}
#iterating through vehicle registration numbers
print("---------------------------------------------------------------------------------")
for regis in regis_num:
    #displaying vehicle registration number
    print("Vehicle Registration Number:", regis)
    #extracting state code
    state_code=regis[:2]
    print("State Code:", state_code)
    #extracting district code
    district_code=regis[2:4]
    print("District Code:", district_code)
    #extracting series
    series=regis[4:6]
    print("Series:", series)
    #extracting vehicle number
    vehicle_num=regis[6:10]
    print("Vehicle Number:", vehicle_num)
    #counting letters and digits
    letters=0
    digits=0
    for i in regis:
        if i.isalpha():
            letters+=1
        elif i.isdigit():
            digits+=1
    print("Letters:", letters)
    print("Digits:", digits)
    #validating format
    if regis[0:2].isalpha() and regis[2:4].isdigit() and regis[4:6].isalpha() and regis[6:10].isdigit() and letters==4 and digits==6:
        print("Registration Status: Valid")
    else:
        print("Registration Status: Invalid")
    print("-------------------------------------------------------------------------------")
    #updating state-wise vehicle count
    print("Displaying state-wise vehicle count:")
    if state_code in state_count:
        state_count[state_code]+=1
    else:
        state_count[state_code]=1
#displaying state-wise vehicle count
for state, count in state_count.items():
    print(state, "->", count)
print("---------------------------------------------------------------------------------")
#displaying invalid registrations
for regis in regis_num:
    if regis[0:2].isalpha() and regis[2:4].isdigit() and regis[4:6].isalpha() and regis[6:10].isdigit() and letters==4 and digits==6:
        print("Registration Status: Valid")
    else:
        print("Registration Status: Invalid")
        print("Vehicle Registration Number:", regis)
print("---------------------------------------------------------------------------------")
print("Challenge: Generate a state-wise report:")
for state, count in state_count.items():
    print(state, "->", count)
