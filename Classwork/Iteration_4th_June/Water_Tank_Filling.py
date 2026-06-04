#A water tank is being filled with water at a constant rate of 10 liters per minute. Initially, the tank contains 0 liters of water.
#Write a program that displays the amount of water in the tank after each minute and continues until the tank reaches 100 liters.
#initialize water amount in the tank
water_amount=0
time=0
#loop until water amount reaches 100 liters
while(water_amount<=100):
    print("Water amount in the tank  at time ", time,"minute(s)" ": ", water_amount, "liters")
    water_amount+=10
    time+=1
#--------------------------------------------------------------
print("Tank is full ...")