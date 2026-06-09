#importing 2D_figure_area_perimeter_calculator module
import area_perimeter_calculator_2Dfigure as area_perimeter
#program to calculate area and perimeter of a rectangle
#taking input from user for length
length=int(input("Enter length of rectangle : "))
#validating the input
if length<=0:
    exit("Please enter a positive number for length...Exited")
#taking input from user for breadth
breadth=int(input("Enter breadth of rectangle : "))
#validating the input
if breadth<=0:
    exit("Please enter a positive number for breadth...Exited")
#-----------------------------------------------------------
#calling function to calculate area of rectangle
area=area_perimeter.area_rectangle(length, breadth)
#calling function to calculate perimeter of rectangle
perimeter=area_perimeter.perimeter_rectangle(length, breadth)
#displaying area and perimeter of rectangle
print("Area of rectangle is : ", area)
print("Perimeter of rectangle is : ", perimeter)
#-----------------------------------------------------------
print("---------------------------------------------")
#program to calculate area and perimeter of a square
#taking input from user for side
side=int(input("Enter side of square : "))
#validating the input
if side<=0:
    exit("Please enter a positive number for side...Exited")
#-----------------------------------------------------------
#calling function to calculate area of square
area=area_perimeter.area_square(side)
#calling function to calculate perimeter of square
perimeter=area_perimeter.perimeter_square(side)
#displaying area and perimeter of square
print("Area of square is : ", area)
print("Perimeter of square is : ", perimeter)
#-----------------------------------------------------------
print("---------------------------------------------")
#program to calculate area and perimeter of a circle
#taking input from user for radius
radius=int(input("Enter radius of circle : "))
#validating the input
if radius<=0:
    exit("Please enter a positive number for radius...Exited")
#-----------------------------------------------------------
#calling function to calculate area of circle
area=area_perimeter.area_circle(radius)
#calling function to calculate perimeter of circle
perimeter=area_perimeter.perimeter_circle(radius)
#displaying area and perimeter of circle
print("Area of circle is : ", area)
print("Perimeter of circle is : ", perimeter)   