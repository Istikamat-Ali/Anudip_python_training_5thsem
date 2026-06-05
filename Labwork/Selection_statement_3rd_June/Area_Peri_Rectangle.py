#Program to calculate area and perimeter of a rectangle
#input of length and breadth of a rectangle
print("-------------------Rectangle-----------------------")
length=int(input("Enter the length of the rectangle (in cm): "))
#check length is negative
if(length<0):
    exit("Length cannot be negative .... Exited")   
breadth=int(input("Enter the breadth of the rectangle (in cm): "))
#check breadth is negative
if(breadth<0):
    exit("Breadth cannot be negative .... Exited")
print("---------------------------------------------")
print("The length of the rectangle is: ", length, "cm")
print("The breadth of the rectangle is: ", breadth, "cm")
print("---------------------------------------------")
#To calculate perimeter
perimeter=2*(length+breadth)
#To calculate area
area=length*breadth
#Displaying perimeter and area of the rectangle
print("Perimeter of the rectangle : ", perimeter, "cm\n","Area of the rectangle : ", area, "cm^2")
