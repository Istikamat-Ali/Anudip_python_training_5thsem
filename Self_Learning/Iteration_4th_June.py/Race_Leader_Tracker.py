# 6.> program to track race leaders
# The program takes the number of racers and their lap times as input, and then finds the fastest and slowest lap times, their positions, and the difference between them.
# Position starts from 1, not 0.
print("---------------- Race Leader Tracker ----------------")
# input number of racers from user
N = int(input("Enter the number of racers: "))
#validating the input
if N <= 0:
    exit("Please enter a positive number for the number of racers...Exited")
print("Enter the lap times of the racers one by one:")
# taking first lap time as initial fastest and slowest
time = float(input("Enter lap time for racer 1: "))
# validating the input
if time < 0:
    exit("Please enter a positive lap time...Exited")
fastest_time = time # initializing fastest time with the first lap time
slowest_time = time # initializing slowest time with the first lap time

fastest_position = 1 # initializing fastest position with the first racer
slowest_position = 1 # initializing slowest position with the first racer

# reading remaining lap times and finding fastest and slowest
for i in range(2, N + 1):# starting from 2 since we have already taken the first lap time as input
    time = float(input("Enter lap time for racer " + str(i) + ": "))
    # validating the input
    if time < 0:
        exit("Please enter a positive lap time...Exited")
#------------------------------------------------------------------------
    if time < fastest_time:      # comparing current time with fastest time
        fastest_time = time      # updating fastest time if current time is faster
        fastest_position = i     # updating fastest position
#------------------------------------------------------------------------
    if time > slowest_time:      # comparing current time with slowest time
        slowest_time = time      # updating slowest time if current time is slower
        slowest_position = i     # updating slowest position

print("-------------------------------------------------------------")

# calculating the difference between fastest and slowest lap times
time_difference = slowest_time - fastest_time

# displaying the results
print("Fastest Racer Position:", fastest_position)
print("Slowest Racer Position:", slowest_position)
print("Difference between Fastest and Slowest Lap Time:", time_difference) 