#program to calculate simple interest 
#input of principal amount, rate of interest and time in year
print("-------------------Simple Interest-----------------------")
principal=int(input("Enter the principal amount (in Rs): "))
#check principal amount is negative
if (principal<0):
    exit("Principal amount cannot be negative .... Exited")
rate=int(input("Enter the rate of interest (in %): "))
#check rate of interest is negative
if (rate<0):
    exit("Rate of interest cannot be negative .... Exited")
time=int(input("Enter the time (in year): "))
#check time is negative
if (time<0):
    exit("Time cannot be negative .... Exited")
print("---------------------------------------------------")

#calculate simple interest
simple_interest=(principal*rate*time)/100
print("---------------------------------------------")
print("Principal Amount : ", principal, "Rs", "   Rate of Interest : ", rate, "%", "   Time : ", time, "year")
print("---------------------------------------------")
print("Simple Interest : ", simple_interest, "Rs")