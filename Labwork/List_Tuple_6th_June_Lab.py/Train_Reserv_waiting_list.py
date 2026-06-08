'''10. Train Reservation Waiting List
Problem Statement
Passenger records:
passengers = [
 ("Anuj", "Confirmed"),
 ("Rahul", "Waiting"),
 ("Priya", "Confirmed"),
 ("Amit", "Waiting"),
 ("Neha", "Confirmed")
]
Write a program to:
• Display all waiting-list passengers. 
• Count confirmed and waiting passengers. 
• Find whether a specific passenger has a confirmed ticket. 
• Create separate lists for confirmed and waiting passengers.'''
print("---------------------- Train Reservation Waiting List ----------------------")
# Given list representing passenger records
passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]
print("-------------------------------------------------")
# ------------------------------------------------------------------------
print("---------------- Display All Waiting List Passengers ----------------------")
# ------------------------------------------------------------------------
# Display all waiting-list passengers
for name, status in passengers:
    if status == "Waiting":
        print(name)
print("-------------------------------------------------")
# ------------------------------------------------------------------------
print("---------------- Count Confirmed and Waiting Passengers ----------------------")
# ------------------------------------------------------------------------
# Count confirmed and waiting passengers
confirmed_count = 0
waiting_count = 0
for name, status in passengers:
    if status == "Confirmed":
        confirmed_count += 1
    elif status == "Waiting":
        waiting_count += 1
print("Confirmed Passengers:", confirmed_count)
print("Waiting Passengers:", waiting_count)
print("-------------------------------------------------")
# ------------------------------------------------------------------------
print("---------------- Find Whether a Specific Passenger Has a Confirmed Ticket ----------------------")
# ------------------------------------------------------------------------
# Find whether a specific passenger has a confirmed ticket
search_name = input("Enter Passenger Name: ")
found = False
for name, status in passengers:
    if name == search_name:
        print(search_name, "has a confirmed ticket.")
        found = True
        break
if not found:
    print(search_name, "does not have a confirmed ticket.")
print("-------------------------------------------------")
# ------------------------------------------------------------------------
print("---------------- Create Separate Lists for Confirmed and Waiting Passengers ----------------------")
# ------------------------------------------------------------------------
# Create separate lists for confirmed and waiting passengers
confirmed_list = []
waiting_list = []
for name, status in passengers:
    if status == "Confirmed":
        confirmed_list.append(name)
    elif status == "Waiting":
        waiting_list.append(name)
print("Confirmed List:", confirmed_list)
print("Waiting List:", waiting_list)
print("-------------------------------------------------")
# ------------------------------------------------------------------------

