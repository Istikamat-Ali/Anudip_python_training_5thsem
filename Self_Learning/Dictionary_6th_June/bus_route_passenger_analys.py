'''7. Bus Route Passenger Analysis
Sample Data
passengers = {
 "Stop1": 12,
 "Stop2": 25,
 "Stop3": 18,
 "Stop4": 32,
 "Stop5": 9,
 "Stop6": 28,
 "Stop7": 14,
 "Stop8": 7,
 "Stop9": 21,
 "Stop10": 16
}
Tasks
• Display stops having more than 20 passengers. 
• Count stops with fewer than 10 passengers. 
• Find the busiest stop. 
• Create a list of stops requiring an extra bus (passengers > 25). 
• Calculate the average number of passengers.'''
print("---------------------- Bus Route Passenger Analysis ----------------------")
#Given dictionary for passenger count at each stop
passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}
print("-------------------------------------------------")
# ------------------------------------------------------------------------
# Task 1: Display stops having more than 20 passengers
print("Display stops having more than 20 passengers:")
for stop, passengers in passengers.items():
    if passengers > 20:
        print(stop)
print("-------------------------------------------------")
# ------------------------------------------------------------------------
# Task 2: Count stops with fewer than 10 passengers
print("Count stops with fewer than 10 passengers:")
count = 0
for stop, passengers in passengers.items():
    if passengers < 10:
        count += 1
print("Stops with fewer than 10 passengers:", count)
print("-------------------------------------------------")
# ------------------------------------------------------------------------
# Task 3: Find the busiest stop
print("Find the busiest stop:")
busiest_stop = max(passengers, key=passengers.get)#busiest stop is the key of the maximum value
print("Busiest Stop:", busiest_stop)
print("-------------------------------------------------")
# ------------------------------------------------------------------------
# Task 4: Create a list of stops requiring an extra bus
print("Create a list of stops requiring an extra bus:")
extra_bus_stops = [stop for stop, passengers in passengers.items() if passengers > 25]#generator expression for finding stops requiring an extra bus
print("Stops requiring an extra bus:", extra_bus_stops)
print("-------------------------------------------------")
# ------------------------------------------------------------------------
# Task 5: Calculate the average number of passengers
print("Calculate the average number of passengers:")
total_passengers = sum(passengers.values())
average_passengers = total_passengers / len(passengers) # for average number of passengers
print("Average Number of Passengers:", average_passengers)
print("-------------------------------------------------")
