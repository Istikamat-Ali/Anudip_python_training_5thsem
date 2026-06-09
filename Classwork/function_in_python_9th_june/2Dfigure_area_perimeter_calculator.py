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
    area=3.14*radius*radius
    #return the calculated area
    return area
#-------------------------------------------------------------
#function to calculate perimeter of circle
def perimeter_circle(radius):
    #calculate perimeter
    perimeter=2*3.14*radius
    #return the calculated perimeter
    return perimeter