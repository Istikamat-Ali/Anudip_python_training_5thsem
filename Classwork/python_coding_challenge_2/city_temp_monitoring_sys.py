'''Problem 8: City Temperature Monitoring System
Problem Statement
Daily temperatures of different cities are stored below.
Sample Data
temperature = {
 "Delhi": 41,
 "Mumbai": 33,
 "Chennai": 37,
 "Kolkata": 39,
 "Bengaluru": 28,
 "Pune": 30,
 "Jaipur": 42,
 "Lucknow": 40,
 "Hyderabad": 35,
 "Ahmedabad": 43
}
Tasks
1. Display cities with temperature above 40°C. 
2. Find the hottest city. 
3. Find the coolest city. 
4. Calculate average temperature. 
5. Create a list of pleasant cities (<35°C). 
Sample Output
Cities Above 40°C:
Delhi
Jaipur
Ahmedabad
Hottest City:
Ahmedabad (43°C)
Coolest City:
Bengaluru (28°C)
Average Temperature: 36.8°C
Pleasant Cities:
['Mumbai', 'Bengaluru', 'Pune']'''
#given dictionary of temperature and city name
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}
#display the cities with temperature above 40°C
print("Cities Above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city)
#find the hottest city
print("Hottest City:")
hottest_city_temp=max(temperature.values())
for city, temp in temperature.items():
    if temp==hottest_city_temp:
        hottest_city=city
print(f"{hottest_city} ({temperature[hottest_city]}°C)")
#find the coolest city
print("Coolest City:")
for city, temp in temperature.items():
    if temp==min(temperature.values()):
        coolest_city=city
print(f"{coolest_city} ({temperature[coolest_city]}°C)")
#calculate average temperature
total_temp = sum(temperature.values())
average_temp = total_temp / len(temperature)
print("Average Temperature:", f"{average_temp:.1f}°C")
#create a list of pleasant cities (<35°C)
pleasant_cities = [city for city, temp in temperature.items() if temp < 35] #list comprehension
print("Pleasant Cities:\n", pleasant_cities)
