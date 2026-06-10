#to import interest calculator
import Classwork.function_in_python_9th_june.interest_calculator_module as interest_calculator_module
#---------------Main Function-----------------------
principal=float(int("Enter the principal amount (in Rs): "))
#validating the principal amount
if(principal<0):
    exit("Principal amount cannot be negative .... Exited")
rate=float(int("Enter the rate of interest (in %): "))
#validating the rate of interest
if(rate<0):
    exit("Rate of interest cannot be negative .... Exited")
time=float(int("Enter the time (in year): "))
#validating the time
if(time<0):
    exit("Time cannot be negative .... Exited")
#call the function to calculate simple interest
#----------------------------------------------------
print("---------------------------------------------")
#displaying the interest 
si=interest_calculator_module.simple_interest(principal, rate, time)
print("Principal Amount : ", principal, "Rs", "   Rate of Interest : ", rate, "%", "   Time : ", time, "year")
print("---------------------------------------------")
print("Simple Interest : ", si(principal, rate, time), "Rs")
#display compound interest 
ci=interest_calculator_module.compound_interest(principal, rate, time)
print("---------------------------------------------")
print("Compound Interest : ", ci(principal, rate, time), "Rs")
     