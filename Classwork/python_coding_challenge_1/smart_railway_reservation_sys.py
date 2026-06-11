'''Problem 1: Smart Railway Reservation System
Problem Statement
A railway reservation system stores the booking status of seats in a train coach.
Sample Data
seats = {
 1: "Booked",
 2: "Available",
 3: "Booked",
 4: "Available",
 5: "Booked",
 6: "Booked",
 7: "Available",
 8: "Booked",
 9: "Available",
 10: "Booked"
}
Tasks
1. Display all available seat numbers. 
2. Count booked and available seats. 
3. Reserve the first available seat. 
4. Cancel booking for a given seat number. 
5. Store the updated reservation status in reservations.txt. 
6. Display occupancy percentage. 
Sample Output
Available Seats:
2 4 7 9
Booked Seats: 6
Available Seats: 4
Seat 2 Reserved Successfully.
Occupancy Percentage: 70.0%
Reservation Details Saved Successfully'''
#given seats data
seats = {
 1: "Booked",
 2: "Available",
 3: "Booked",
 4: "Available",
 5: "Booked",
 6: "Booked",
 7: "Available",
 8: "Booked",
 9: "Available",
 10: "Booked"
}
#display all available seat numbers
print("Available Seats:")
for seat, status in seats.items():
    if status == "Available":
        print(seat, end=" ")
print()
#count booked and available seats
booked_seats = 0
available_seats = 0
for status in seats.values():
    if status == "Booked":
        booked_seats += 1
    elif status == "Available":
        available_seats += 1
print("Booked Seats:", booked_seats)
print("Available Seats:", available_seats)
#reserve the first available seat
for seat, status in seats.items():
    if status == "Available":
        seats[seat] = "Booked"
        print("Seat", seat, "Reserved Successfully.")
        break
#cancel booking for a given seat number
seat_to_cancel = int(input("Enter the seat number to cancel: "))
if seat_to_cancel not in seats:
    exit("Invalid seat number.")
seats[seat_to_cancel] = "Available"# make booked seat as available seat for cancel
print("Seat", seat_to_cancel, "Cancelled Successfully.")
#store the updated reservation status in reservations.txt
with open("reservations.txt", "w") as file:
    for seat, status in seats.items():
        file.write(f"Seat {seat}: {status}\n")
#display occupancy percentage
total_seats = len(seats)
occupancy_percentage = (total_seats - available_seats) / total_seats * 100 #booked seats is total_seats - available_seats
print("Occupancy Percentage:", occupancy_percentage)
#