'''1. Railway Reservation Seat Analyzer 
Problem Statement 
A railway coach has seats represented as follows: 
seats = [ 
    "Booked", "Available", "Booked", "Booked", 
    "Available", "Available", "Booked", "Available", 
    "Booked", "Booked", "Available", "Booked" 
] 
Requirements 
Create the following functions: 
1. count_seats(seats) 
Returns the number of booked and available seats. 
2. first_available(seats) 
Returns the seat number of the first available seat. 
3. occupancy_percentage(seats) 
Returns the percentage of occupied seats. 
4. display_available_seats(seats) 
Displays all available seat numbers. 
Sample Output 
Booked Seats: 7 
Available Seats: 5 
 
First Available Seat: 2 
 
Occupancy Percentage: 58.33% 
 
Available Seat Numbers: 
2 5 6 8 11'''
print("---------------------- Railway Reservation Seat Analyzer ----------------------")
#given list representing seat status
seats = ["Booked", "Available", "Booked", "Booked", "Available", "Available", "Booked", "Available", "Booked", "Booked", "Available", "Booked"]
#counting the number of booked and available seats
def count_seats(seats):
    booked_seats = 0
    available_seats = 0
    for seat in seats:
        if seat == "Booked":
            booked_seats += 1
        elif seat == "Available":
            available_seats += 1
    return booked_seats, available_seats
print("Booked Seats:",list(count_seats(seats))[0])
print("Available Seats:",list(count_seats(seats))[1])
print()
print("------------------------------------------------------------------------")
#finding the first available seat
def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            return i + 1#as seat no starts from 1 and indexing from 0
    return None# if no seat is available
print("First Available Seat:",first_available(seats))
print()
print("------------------------------------------------------------------------")
#calculating the occupancy percentage
def occupancy_percentage(seats):
    total_seats = len(seats)
    occupied_seats = 0
    for seat in seats:
        if seat == "Booked":
            occupied_seats += 1
    occupency_percentage=(occupied_seats/total_seats)*100        
    return occupency_percentage
print("Occupancy Percentage:",occupancy_percentage(seats))
print()
print("------------------------------------------------------------------------")
#displaying all available seat numbers
def display_available_seats(seats):
    available_seat_numbers = []
    for i in range(len(seats)):
        if seats[i] == "Available":
            available_seat_numbers.append(i + 1)
    return available_seat_numbers
print("Available Seat Numbers:",display_available_seats(seats))
print()
print("------------------------------------------------------------------------")