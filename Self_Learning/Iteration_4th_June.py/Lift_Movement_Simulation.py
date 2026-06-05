#10.> program to simulate lift movement and calculate floors travelled
print("---------------------Lift Movement Simulation---------------------")
current_floor = 0 # initializing current floor to 0
total_floors_travelled = 0 # initializing total floors travelled to 0
while True:
    destination_floor = int(input("Enter Destination Floor (or -1 to stop): ")) # input destination floor from user
    if destination_floor == -1: # check if the user wants to stop entering destinations
        break
    floors_travelled = abs(destination_floor - current_floor) # calculating floors travelled in the current trip
    print("Travelled:", floors_travelled, "floors") # displaying floors travelled in the current trip
    total_floors_travelled += floors_travelled # adding the floors travelled in the current trip to total
    current_floor = destination_floor # updating current floor to the destination floor for the next iteration
# displaying total floors travelled after the user stops entering destinations
print("Total Floors Travelled:", total_floors_travelled, "floors")  