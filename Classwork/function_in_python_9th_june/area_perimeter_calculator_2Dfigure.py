#program to calculate area and perimeter of a 2D figure
#function to calculate area of rectangle
def area_rectangle(length, breadth):
    #calculate area
    area=length*breadth
    #return the calculated area
    return area
#----------------------------------------------------------
#function to calculate perimeter of rectangle
def perimeter_rectangle(length, breadth):
    #calculate perimeter
    perimeter=2*(length+breadth)
    #return the calculated perimeter
    return perimeter
#-------------------------------------------------------------
#function to calculate area of square
def area_square(side):
    #calculate area
    area=side*side
    #return the calculated area
    return area
#-------------------------------------------------------------
#function to calculate perimeter of square
def perimeter_square(side):
    #calculate perimeter
    perimeter=4*side
    #return the calculated perimeter
    return perimeter
#-------------------------------------------------------------
#function to calculate area of circle
def area_circle(radius):
    #calculate area
    area=3.14*radius*radius#assuming pi=3.14
    #return the calculated area
    return area
#-------------------------------------------------------------
#function to calculate perimeter of circle
def perimeter_circle(radius):
    #calculate perimeter
    perimeter=2*3.14*radius
    #return the calculated perimeter
    return perimeter
#-------------------------------------------------------------
#function to calculate area of a triangle 
def equilateral_area(side):
    #calculate area 
    area=3**0.5/4*side**2
    #return area 
    return area
#-------------------------------------------------------------
#function to calculate perimeter of a triangle
def equilateral_perimeter(side):
    #calculate perimeter
    perimeter=3*side
    #return the calculated perimeter
    return perimeter
#-------------------------------------------------------------
#function to calculate the area of a triangle using herons formula
def heron_area(side1,side2,side3):
    #calculate area using herons formula
    s=(side1+side2+side3)/2
    area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
    #return the calculated area
    return area
#-------------------------------------------------------------
#function to calculate the perimeter of a triangle
def heron_perimeter(side1,side2,side3):
    #calculate perimeter
    perimeter=side1+side2+side3
    #return the calculated perimeter
    return perimeter
#-------------------------------------------------------------
def isosceles_area(base, height):
    #calculate area
    area=0.5*base*height
    #return the calculated area
    return area
#-------------------------------------------------------------
def isosceles_perimeter(side1,side2,side3):
    #calculate perimeter
    perimeter=side1+side2+side3
    #return the calculated perimeter
    return perimeter
#-------------------------------------------------------------
#function to calculate the area of a rhombus
def rhombus_area(diagonal1,diagonal2):
    #calculate area
    area=0.5*diagonal1*diagonal2
    #return the calculated area
    return area
#-------------------------------------------------------------
#function to calculate the perimeter of a rhombus
def rhombus_perimeter(side):
    #calculate perimeter
    perimeter=4*side
    #return the calculated perimeter
    return perimeter
#-------------------------------------------------------------
#function to calculate the area of a parallelogram
def parallelogram_area(base, height):
    #calculate area
    area=base*height
    #return the calculated area
    return area
#-------------------------------------------------------------
#function to calculate the perimeter of a parallelogram
def parallelogram_perimeter(length, breadth):
    #calculate perimeter
    perimeter=2*(length+breadth)
    #return the calculated perimeter
    return perimeter
#-------------------------------------------------------------
#function to calculate the area of a trapezium
def trapezium_area(base1, base2, height):
    #calculate area
    area=0.5*(base1+base2)*height
    #return the calculated area
    return area
#-------------------------------------------------------------
#function to calculate the perimeter of a trapezium
def trapezium_perimeter(side1,side2,side3,side4):
    #calculate perimeter
    perimeter=side1+side2+side3+side4
    #return the calculated perimeter
    return perimeter
#-------------------------------------------------------------
#function to calculate the area of a kite
def kite_area(diagonal1,diagonal2):
    #calculate area
    area=0.5*diagonal1*diagonal2
    #return the calculated area
    return area
#-------------------------------------------------------------
#function to calculate the perimeter of a kite
def kite_perimeter(side1,side2,side3,side4):
    #calculate perimeter
    perimeter=side1+side2+side3+side4
    #return the calculated perimeter
    return perimeter
#-------------------------------------------------------------
#function to calculate the area of ellipse
def area_ellipse(major_axis,minor_axis):
    #calculate area
    area=3.14*major_axis*minor_axis
    #return the calculated area
    return area
#-------------------------------------------------------------
#function to calculate the perimeter of ellipse
def perimeter_ellipse(major_axis,minor_axis):
    #calculate perimeter
    perimeter=3.14*(major_axis+minor_axis)
    #return the calculated perimeter
    return perimeter

     