'''8. Bus Route Monitoring
Problem Statement
Passenger count at each stop:
passengers = [12, 18, 25, 30, 28, 15, 8]
Write a program to:
• Find the busiest stop. 
• Display stops with fewer than 10 passengers. 
• Calculate average passengers. 
• Determine whether any stop exceeded 25 passengers.''' 
print("---------------------- Bus Route Monitoring ----------------------")
# Given list representing passenger count at each stop
passengers = [12, 18, 25, 30, 28, 15, 8]
print("-------------------------------------------------")
# ------------------------------------------------------------------------
print("---------------- Find the Busiest Stop ----------------------")
# ------------------------------------------------------------------------
# Find the busiest stop
busiest_stop = max(passengers)
print("Busiest Stop:", busiest_stop)
print("-------------------------------------------------")
# ------------------------------------------------------------------------
print("---------------- Display Stops with Fewer Than 10 Passengers ----------------------")
# ------------------------------------------------------------------------
# Display stops with fewer than 10 passengers
for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1, "has fewer than 10 passengers")
print("-------------------------------------------------")
# ------------------------------------------------------------------------
print("---------------- Calculate Average Passengers ----------------------")
# ------------------------------------------------------------------------
# Calculate average passengers
total_passengers = sum(passengers)
average_passengers = total_passengers / len(passengers)
print("Average Passengers:", average_passengers)
print("-------------------------------------------------")
# ------------------------------------------------------------------------
print("---------------- Determine Whether Any Stop Exceeded 25 Passengers ----------------------")
# ------------------------------------------------------------------------
# Determine whether any stop exceeded 25 passengers
for i in range(len(passengers)):    
    if passengers[i] > 25:
        print("Stop", i + 1, "exceeded 25 passengers")
print("-------------------------------------------------")
# ------------------------------------------------------------------------
print("---------------- End of Bus Route Monitoring ----------------------")
# ------------------------------------------------------------------------
