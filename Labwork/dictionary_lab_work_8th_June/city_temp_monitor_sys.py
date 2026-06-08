'''3. City Temperature Monitoring System
Problem Statement
Daily temperatures of different cities are stored as:
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
1. Display cities having temperature above 40°C. 
2. Find the hottest city. 
3. Find the coolest city. 
4. Calculate average temperature. 
5. Create a list of pleasant cities (temperature < 35°C). 
6. Count cities with temperature between 35°C and 40°C. 
Sample Output
Cities Above 40°C:
Delhi
Jaipur
Ahmedabad
Hottest City: Ahmedabad (43°C)
Coolest City: Bengaluru (28°C)
Average Temperature: 36.8°C
Pleasant Cities:
['Mumbai', 'Bengaluru', 'Pune']
Cities Between 35°C and 40°C: 4'''
print("---------City Temperature Monitoring System----------")
#given dictionary
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
print("-------------------------------------------------------------")
#display cities having temperature above 40°C
print("Cities Above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city)
print("-------------------------------------------------------------")
#find the hottest city
hottest_city = max(temperature, key=temperature.get)# for hottest city it returns the key of the maximum value
print("Hottest City:", hottest_city, "(", temperature[hottest_city], "°C)")
print("-------------------------------------------------------------")
#find the coolest city
coolest_city = min(temperature, key=temperature.get)# for coolest city it returns the key of the minimum value
print("Coolest City:", coolest_city, "(", temperature[coolest_city], "°C)")
print("-------------------------------------------------------------")
#calculate average temperature
total_temp = sum(temperature.values())
average_temp = total_temp / len(temperature)# for average temperature it returns the sum of all values divided by the number of values
print("Average Temperature:", average_temp, "°C")
print("-------------------------------------------------------------")
#creating a list of pleasant cities
pleasant_cities = [city for city, temp in temperature.items() if temp < 35]# generator expression for finding pleasant cities
print("Pleasant Cities:")
print(pleasant_cities)
print("-------------------------------------------------------------")
#count cities with temperature between 35°C and 40°C
count_cities = sum(1 for temp in temperature.values() if 35 <= temp <= 40)#generator expression for count
print("Cities Between 35°C and 40°C:", count_cities)
print("-------------------------------------------------------------")