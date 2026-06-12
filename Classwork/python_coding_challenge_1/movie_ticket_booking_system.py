'''roblem 7: Movie Ticket Booking System 
Problem Statement 
Seat booking status in a cinema hall is stored as follows. 
Sample Data 
tickets = { 
    "A1": "Booked", 
    "A2": "Available", 
    "A3": "Booked", 
    "A4": "Available", 
    "B1": "Booked", 
    "B2": "Available", 
    "B3": "Booked", 
    "B4": "Available", 
    "C1": "Booked", 
    "C2": "Available" 
} 
Tasks 
1. Display available seats.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Save updated booking details to tickets.txt.  
5. Calculate hall occupancy percentage.  
Sample Output 
Available Seats: 
A2 
A4 
B2 
B4 
C2 
 
Booked Seats: 5 
Available Seats: 5 
 
Seat A2 Reserved Successfully. 
 
Hall Occupancy Percentage: 60.0% 
 
Booking Details Saved Successfully'''
print("---------------------- Movie Ticket Booking System ----------------------")
#given dictionary for movie ticket booking system
tickets = {
    "A1": "Booked",
    "A2": "Available",
    "A3": "Booked",
    "A4": "Available",
    "B1": "Booked",
    "B2": "Available",
    "B3": "Booked",
    "B4": "Available",
    "C1": "Booked",
    "C2": "Available"
}
#display available seats
print("Available Seats:")
for seat, status in tickets.items():
    if status == "Available":
        print(seat)
#count booked and available seats
booked_seats = 0
available_seats = 0
for status in tickets.values():
    if status == "Booked":
        booked_seats += 1
    elif status == "Available":
        available_seats += 1
print("Booked Seats:", booked_seats)
print("Available Seats:", available_seats)
print()
#reserve the first available seat
for seat, status in tickets.items():
    if status == "Available":
        tickets[seat] = "Booked"
        print("Seat", seat, "Reserved Successfully.")
        break
print()
#save updated booking details to tickets.txt
with open("tickets.txt", "w") as file:
    for seat, status in tickets.items():
        file.write(f"Seat {seat}: {status}\n")
print("Booking Details Saved Successfully")
print()
#calculate hall occupancy percentage
total_seats = len(tickets)
occupancy_percentage = (total_seats - available_seats) / total_seats * 100 #booked seats is total_seats - available_seats
print("Hall Occupancy Percentage:", occupancy_percentage)
