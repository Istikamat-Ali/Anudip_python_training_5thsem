'''
Problem Statement

A bus has seats represented as:
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

Where:
1 → Seat Booked
0 → Seat Available

Write a program to:
1. Count booked and available seats.
2. Find the first available seat and stop searching immediately.
3. Create a list of all available seat numbers.
4. Determine whether the bus is more than 70% occupied.
'''

print("---------------------- Bus Seat Reservation Analysis ----------------------")

# Given list representing seat status
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# ------------------------------------------------------------------------
print("---------------- Count Booked and Available Seats ----------------------")
# ------------------------------------------------------------------------

# Initialize counters
booked_seats = 0
available_seats = 0

# Count booked and available seats
for seat in seats:

    if seat == 1:
        booked_seats += 1

    else:
        available_seats += 1

print("Total Booked Seats:", booked_seats)
print("Total Available Seats:", available_seats)

print("------------------------------------------------------------------------")

# ------------------------------------------------------------------------
print("-------------------- First Available Seat ------------------------------")
# ------------------------------------------------------------------------

# Find the first available seat and stop searching
for i in range(len(seats)):

    if seats[i] == 0:
        print("First Available Seat Number:", i + 1)
        break

print("------------------------------------------------------------------------")

# ------------------------------------------------------------------------
print("-------------------- List of Available Seats ---------------------------")
# ------------------------------------------------------------------------

# Create an empty list to store available seat numbers
available_seat_numbers = []

# Find all available seats
for i in range(len(seats)):

    if seats[i] == 0:
        available_seat_numbers.append(i + 1)

print("Available Seat Numbers:", available_seat_numbers)

print("------------------------------------------------------------------------")

# ------------------------------------------------------------------------
print("--------------------- Bus Occupancy Status -----------------------------")
# ------------------------------------------------------------------------

# Calculate occupancy percentage
occupancy_percentage = (booked_seats * 100) / len(seats)

print("Occupancy Percentage:", occupancy_percentage, "%")

# Check if occupancy is more than 70%
if occupancy_percentage > 70:
    print("Bus is more than 70% occupied.")

else:
    print("Bus is not more than 70% occupied.")

print("------------------------------------------------------------------------")

