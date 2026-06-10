#import module numeric calculations
from numericcalculation import *
#----------------------------------
#main program
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
#to calculate addition
print("Addition : ",add(num1, num2))
#to calculate subtraction
print("Difference between",num1," and ",num2,"is : ",subtract(num1, num2))
#to calculate multiplication
print("Multiplication : ",multiply(num1, num2))
#to calculate division
print("Division : ",divide(num1, num2))
#to calculate remainder after division
print("Remainder after division : ",modulus(num1, num2))
#to calculate exponentiation
print("Exponentiation : ",exponentiation(num1, num2))
#to calculate floor division
print("Floor division : ",floor_division(num1, num2))
