#Program to check whether three angles can form a triangle or not
print("-------------------Triangle Formation-----------------------")
#input enter first angle of a triangle
angle1=float(input("Enter the first angle (in degree): "))
#validate angle1
if (angle1<=0):
    exit("Angle must be positive .... Exited")
#-------------------------------------------------------------------
#input enter second angle of a triangle
angle2=float(input("Enter the second angle (in degree): "))
#validate angle2
if (angle2<=0):
    exit("Angle must be positive .... Exited")
#-------------------------------------------------------------------
#input enter third angle of a triangle
angle3=float(input("Enter the third angle (in degree): "))
#validate angle3
if (angle3<=0):
    exit("Angle must be positive .... Exited")
#-------------------------------------------------------------------
print("---------------------------------------------")
#verifying Triangle Formation
if (angle1+angle2+angle3==180):
    #triangle is formed
    if(angle1<90 and angle2<90 and angle3<90):#acute angled triangle
        print("Above angles form an acute angle ")
    elif(angle1==90 or angle2==90 or angle3==90):#right angled triangle 
        print("Above angles form a right angled triangle")
    else:
        print("Above angles form an obtuse angle ")
    
else:
    print("Above angles do not form a triangle")