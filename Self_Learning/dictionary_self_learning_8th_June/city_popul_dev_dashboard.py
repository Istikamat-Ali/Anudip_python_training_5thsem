'''5. City Population & Development Dashboard
Problem Statement
The government wants to analyze city data.
Store details of at least 30 cities.
Example Structure
cities = {
 "Delhi": {
 "population": 32000000,
 "area": 1484,
 "literacy": 89
 }
}
Requirements
1. Display all city details. 
2. Find the most populated city. 
3. Find the least populated city. 
4. Calculate average population. 
5. Display cities with literacy rate above 90%. 
6. Display cities with literacy below average. 
7. Calculate population density. 
8. Find city with highest density. 
9. Categorize cities: 
o Small 
o Medium 
o Large 
10. Create a development-priority list. 
11. Generate separate dictionaries for: 
o High Literacy Cities 
o Low Literacy Cities 
12. Generate a national summary report. 
Challenge
Rank all cities based on population density.
Assignment Rule (Important)
For all 5 Questions:
• Use at least 30 records. 
• Do not use built-in sorting functions (sorted(), sort()). 
• Use loops and conditions to find maximum, minimum, rankings, and reports. 
• Display results in a structured format. 
• Add a menu-driven interface using while loop.'''
print("------- City Population & Development Dashboard -------")
# taking input from user in this format
'''cities = {
 "Delhi": {
 "population": 32000000,
 "area": 1484,
 "literacy": 89
 }
}'''
cities = {}
for i in range(30):
    city = input("Enter city name: ")
    population = int(input("Enter population: "))
    area = int(input("Enter area: "))
    literacy = float(input("Enter literacy: "))
    cities[city] = {"population": population, "area": area, "literacy": literacy}
print("--------------------------------------------------------------------------")
# Task 1: Display all city details
# --------------------------------------------------
print("All City Details:")
for city, details in cities.items():
    print(f"City: {city}")
    print(f"Population: {details['population']}")
    print(f"Area: {details['area']}")
    print(f"Literacy: {details['literacy']}")
print("--------------------------------------------------------------------------")
# Task 2: Find the most populated city
# --------------------------------------------------
print("Most Populated City:")
most_populated_city = max(cities, key=lambda city: cities[city]["population"])#for city in cities if details["population"] > most_populated
print(f"City: {most_populated_city}")
print(f"Population: {cities[most_populated_city]['population']}")
print(f"Area: {cities[most_populated_city]['area']}")
print(f"Literacy: {cities[most_populated_city]['literacy']}")
print("--------------------------------------------------------------------------")
# Task 3: Find the least populated city
# --------------------------------------------------
print("Least Populated City:")
least_populated_city = min(cities, key=lambda city: cities[city]["population"])#for city in cities if details["population"] < least_populated
print(f"City: {least_populated_city}")
print(f"Population: {cities[least_populated_city]['population']}")
print(f"Area: {cities[least_populated_city]['area']}")
print(f"Literacy: {cities[least_populated_city]['literacy']}")
print("--------------------------------------------------------------------------")
# Task 4: Calculate average population
# --------------------------------------------------
print("Average Population:")
total_population = sum(cities[city]["population"] for city in cities)
average_population = total_population / len(cities)
print(f"Average Population: {average_population}")
print("--------------------------------------------------------------------------")
# Task 5: Display cities with literacy rate above 90%
# --------------------------------------------------
print("Cities with literacy rate above 90%:")
for city, details in cities.items():
    if details["literacy"] > 90:
        print(f"City: {city}")
        print(f"Population: {details['population']}")
        print(f"Area: {details['area']}")
        print(f"Literacy: {details['literacy']}")
print("--------------------------------------------------------------------------")
# Task 6: Display cities with literacy below average
# --------------------------------------------------
print("Cities with literacy below average:")
average_literacy = sum(cities[city]["literacy"] for city in cities) / len(cities)
for city, details in cities.items():
    if details["literacy"] < average_literacy:
        print(f"City: {city}")
        print(f"Population: {details['population']}")
        print(f"Area: {details['area']}")
        print(f"Literacy: {details['literacy']}")
print("--------------------------------------------------------------------------")
# Task 7: Calculate population density
# --------------------------------------------------
print("Population Density:")
for city, details in cities.items():
    population_density = details["population"] / details["area"]#calc population density
    print(f"City: {city}")
    print(f"Population Density: {population_density}")
print("--------------------------------------------------------------------------")
# Task 8: Find city with highest density
# --------------------------------------------------
print("City with highest density:")
highest_density = max(cities, key=lambda city: cities[city]["population"] / cities[city]["area"])
print(f"City: {highest_density}")
print(f"Population Density: {cities[highest_density]['population'] / cities[highest_density]['area']}")
print("--------------------------------------------------------------------------")
# Task 9: Categorize cities
# --------------------------------------------------
print("Categorized Cities:")
for city, details in cities.items():
    population_density = details["population"] / details["area"]
    if population_density > 1000:
        print(f"City: {city}")
        print(f"Population Density: {population_density}")
        print("Category: Large")
    elif population_density > 500:
        print(f"City: {city}")
        print(f"Population Density: {population_density}")
        print("Category: Medium")
    else:
        print(f"City: {city}")
        print(f"Population Density: {population_density}")
        print("Category: Small")
print("--------------------------------------------------------------------------")
# Task 10: Create a development-priority list
# --------------------------------------------------
print("Development Priority List:")
development_priority = sorted(cities, key=lambda city: cities[city]["literacy"], reverse=True)#sorted in descending order
for city in development_priority:
    print(f"City: {city}")
    print(f"Literacy: {cities[city]['literacy']}")
print("--------------------------------------------------------------------------")
# Task 11: Generate separate dictionaries for: High Literacy Cities & Low Literacy Cities
# --------------------------------------------------
high_literacy_cities = {city: details for city, details in cities.items() if details["literacy"] > 90}#generator expression in dictionary for high literacy
low_literacy_cities = {city: details for city, details in cities.items() if details["literacy"] < 90}#generator expression in dictionary for low literacy
print("High Literacy Cities:")
for city, details in high_literacy_cities.items():
    print(f"City: {city}")
    print(f"Population: {details['population']}")
    print(f"Area: {details['area']}")
    print(f"Literacy: {details['literacy']}")
print("--------------------------------------------------------------------------")
print("Low Literacy Cities:")
for city, details in low_literacy_cities.items():
    print(f"City: {city}")
    print(f"Population: {details['population']}")
    print(f"Area: {details['area']}")
    print(f"Literacy: {details['literacy']}")
print("--------------------------------------------------------------------------")
# Task 12: Generate a national summary report
# --------------------------------------------------
print("National Summary Report:")
total_population = sum(cities[city]["population"] for city in cities)
total_area = sum(cities[city]["area"] for city in cities)
average_literacy = sum(cities[city]["literacy"] for city in cities) / len(cities)#for city in cities if details["literacy"] < average_literacy
print(f"Total Population: {total_population}")
print(f"Total Area: {total_area}")
print(f"Average Literacy: {average_literacy}")
print("--------------------------------------------------------------------------")
print("Thank you for using the City Population & Development Dashboard.")


