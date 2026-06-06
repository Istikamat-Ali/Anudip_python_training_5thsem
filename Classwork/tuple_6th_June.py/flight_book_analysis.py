'''Problem Statement
A flight reservation system stores passenger records as tuples:
bookings = (
 ("P101", "Delhi", "Confirmed"),
 ("P102", "Mumbai", "Waiting"),
 ("P103", "Delhi", "Confirmed"),
 ("P104", "Chennai", "Cancelled"),
 ("P105", "Mumbai", "Confirmed"),
 ("P106", "Delhi", "Waiting")
)
Where:
• Passenger ID 
• Destination 
• Booking Status 
Tasks
Write a Python program to:
1. Display all passengers whose booking status is Confirmed. 
2. Count the number of passengers travelling to Delhi. 
3. Count Confirmed, Waiting, and Cancelled bookings separately. 
4. Create a list containing passenger IDs with Waiting status. 
5. Determine which destination has the highest number of bookings. 

Sample Output
Confirmed Passengers:
P101 Delhi
P103 Delhi
P105 Mumbai
Passengers Travelling to Delhi: 3
Confirmed: 3
Waiting: 2
Cancelled: 1
Waiting List:
['P102', 'P106']
Most Booked Destination:
Delhi'''
print("---------------------- Flight Booking Analysis ----------------------")
#given tuple of bookings
bookings = (
 ("P101", "Delhi", "Confirmed"),
 ("P102", "Mumbai", "Waiting"),
 ("P103", "Delhi", "Confirmed"),
 ("P104", "Chennai", "Cancelled"),
 ("P105", "Mumbai", "Confirmed"),
 ("P106", "Delhi", "Waiting")
)
#Task 1: Display all passengers whose booking status is Confirmed
print("Confirmed Passengers : ")
for record in bookings:
  if(record[2] == "Confirmed"):
    print(record[0],record[1])
print("---------------------------------")
#-----------------------------------------
#Task 2: Count the number of passengers travelling to Delhi
#initializing count variable to 0 for counting passengers travelling to Delhi
count = 0
for record in bookings:
  if(record[1] == "Delhi"):#if destination is Delhi
    count+=1
print("Passengers Travelling to Delhi : ",count)
print("---------------------------------")
#-----------------------------------------
#Task 3: Count Confirmed, Waiting, and Cancelled bookings separately
confirmed = 0
waiting = 0
cancelled = 0
for record in bookings:
  if(record[2] == "Confirmed"):
    confirmed+=1
  elif(record[2] == "Waiting"):
    waiting+=1
  elif(record[2] == "Cancelled"):
    cancelled+=1
print("Confirmed : ",confirmed)
print("Waiting : ",waiting)
print("Cancelled : ",cancelled)
print("---------------------------------")
#-----------------------------------------
#Task 4: Create a list containing passenger IDs with Waiting status
print("Waiting List : ")
#taking an empty variable for waiting list
#initialized waiting list
waiting_list = []
for record in bookings:
  if(record[2] == "Waiting"):
    waiting_list.append(record[0])
print(waiting_list)
print("---------------------------------")
#-----------------------------------------
#Task 5: Determine which destination has the highest number of bookings
#initializing highest count variable to 0 for finding highest count
#initializing count variable to 0 for counting passengers travelling to Delhi, Mumbai and Chennai
delhi = 0
mumbai = 0
chennai = 0
#finding count for all destinations
for record in bookings:
    if record[1] == "Delhi":
        delhi += 1
    elif record[1] == "Mumbai":
        mumbai += 1
    elif record[1] == "Chennai":
        chennai += 1
#checking which destination has the highest count
if delhi >= mumbai and delhi >= chennai:
    print("Most Booked Destination : Delhi")

elif mumbai >= delhi and mumbai >= chennai:
    print("Most Booked Destination : Mumbai")

else:
    print("Most Booked Destination : Chennai")