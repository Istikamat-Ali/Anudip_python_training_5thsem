#program to check whether the tree sides form a triangle or not
#input the fist side 
print("---------------Triangle Formation Check----------------")
side1=int(input("Enter the first side of a triangle (in cm): "))
#validating the first side
if (side1<=0):
    exit("Side must be positive ...Exited")
#------------------------------------------------------------------
side2=int(input("Enter the second side of a triangle (in cm): "))
#validating the second side
if(side2<=0):
    exit("Side must be positive ...Exited")
#------------------------------------------------------------------
side3=int(input("Enter the third side of a triangle (in cm): "))
#validating the third side
if(side3<=0):
    exit("Side must be positive ...Exited")
#------------------------------------------------------------------
print("---------------------------------------------")
print("First side : ", side1, "cm")
print("Second side : ", side2, "cm")
print("Third side : ", side3, "cm")
print("---------------------------------------------")
#check whether the three sides form a triangle or not
if((side1+side2>side3) and (side2+side3>side1) and (side3+side1>side2)):
    print("The three sides form a triangle")
else:    
    print("The three sides do not form a triangle")