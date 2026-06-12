'''Problem 2: Airport Baggage Screening System
Problem Statement
Passenger baggage weights (in kg) are stored as tuples:
baggage = (
 ("P101", 18),
 ("P102", 32),
 ("P103", 24),
 ("P104", 36),
 ("P105", 28),
 ("P106", 20),
 ("P107", 41),
 ("P108", 26),
 ("P109", 19),
 ("P110", 34)
)
Tasks
1. Display passengers carrying baggage above 30 kg. 
2. Count passengers within and exceeding limits. 
3. Calculate excess baggage charges (₹500 per kg above 30 kg). 
4. Create a list of passengers requiring manual inspection. 
5. Find the passenger carrying the heaviest baggage. 
Sample Output
Passengers Exceeding 30 kg Limit:
P102
P104
P107
P110
Passengers Within Limit: 6
Passengers Exceeding Limit: 4
Excess Baggage Charges:
P102 : ₹1000
P104 : ₹3000
P107 : ₹5500
P110 : ₹2000
Passenger with Heaviest Baggage:
P107 (41 kg)
Passengers Requiring Manual Inspection:
['P102', 'P104', 'P107', 'P110']'''
#Given tuples of passenger baggage weights 
baggage = (
    ("P101", 18),
    ("P102", 32),
    ("P103", 24),
    ("P104", 36),
    ("P105", 28),
    ("P106", 20),
    ("P107", 41),
    ("P108", 26),
    ("P109", 19),
    ("P110", 34)
)
# Display passengers carrying baggage above 30 kg
print("Passengers Exceeding 30 kg Limit:")
for passenger, weight in baggage:
    if weight > 30:
        print(passenger)
# Count passengers within and exceeding limits
passengers_within_limit = 0
passengers_exceeding_limit = 0
for passenger, weight in baggage:
    if weight <= 30:
        passengers_within_limit += 1
    else:
        passengers_exceeding_limit += 1
print("Passengers Within Limit:", passengers_within_limit)
print("Passengers Exceeding Limit:", passengers_exceeding_limit)
# Calculate excess baggage charges
print("Excess Baggage Charges:")
for passenger, weight in baggage:
    if weight > 30:
        print(f"{passenger} : Rs.{((weight - 30) * 500)}")
# Find the passenger carrying the heaviest baggage
print("Passenger with Heaviest Baggage:")
heaviest_passenger = None
heaviest_weight = 0
for passenger, weight in baggage:
    if weight > heaviest_weight:
        heaviest_passenger = passenger
        heaviest_weight = weight
print(f"{heaviest_passenger} ({heaviest_weight} kg)")
# Create a list of passengers requiring manual inspection
print("Passengers Requiring Manual Inspection:") # if weight>30
manual_inspection = []
for passenger, weight in baggage:
    if weight > 30:
        manual_inspection.append(passenger)
print(manual_inspection)