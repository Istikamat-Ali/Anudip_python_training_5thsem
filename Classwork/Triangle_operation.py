#Program to calculatearea and perimeter of a triangle
#input of three sides of a triangle
print("-------------------Triangle-----------------------")
side1=int(input("Enter the first side (in cm): "))
side2=int(input("Enter the second side (in cm): "))
side3=int(input("Enter the third side (in cm): "))
#---------------------------------------------------
print("---------------------------------------------")
print("The first side of the triangle is: ", side1, "cm")
print("The second side of the triangle is: ", side2, "cm")
print("The third side of the triangle is: ", side3, "cm")
#To calculate perimeter
perimeter=side1+side2+side3
#---------------------------------------------------
#To calculate area using Heron's formula
s=perimeter/2
#Displaying Area
print("Area of the triangle is: ", (s*(s-side1)*(s-side2)*(s-side3))**0.5, "cm^2")
#Displaying Perimeter
print("Perimeters of the triangle is: ", perimeter, "cm")