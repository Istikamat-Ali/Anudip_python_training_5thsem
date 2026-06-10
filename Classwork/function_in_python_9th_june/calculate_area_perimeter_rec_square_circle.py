'''create a python program which provides a menu to user to selectthe 2D figure (rectangle,square,circle)
.After selecting the figure user is again asked to provide the input details of corresponding for the figure .
After input of coresponding data again proovide a menu to select the operation (area,perimeter) and as per date 
provided by user for operations and selected figure.Display thr result of operation selected  and this task is repeated again 
and again until user select option to exit from this figure
'''

# ==========================================================
# PROGRAM : 2D FIGURE AREA & PERIMETER CALCULATOR
# PURPOSE : Calculate Area or Perimeter of various 2D figures
# MODULE   : area_perimeter_calculator_2Dfigure.py
# ==========================================================
# import module with aliasing as ap
import area_perimeter_calculator_2Dfigure as ap
# repeating program until user chooses Exit
while True:

    # ======================================================
    #                  DISPLAY MAIN MENU
    # ======================================================
    print("\n" + "=" * 50)
    print("          2D FIGURE AREA & PERIMETER CALCULATOR")
    print("=" * 50)

    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Triangle")
    print("5. Rhombus")
    print("6. Parallelogram")
    print("7. Trapezium")
    print("8. Kite")
    print("9. Ellipse")
    print("10. Exit")

    # take figure choice
    figure_choice = int(input("\nEnter your choice : "))

    # ======================================================
    #                     EXIT OPTION
    # ======================================================
    if figure_choice == 10:
        exit("\nThank You For Using The Program.")
    while True:
        if figure_choice==1:
        # ======================================================
        #                      RECTANGLE 
        # ======================================================
        #taking input from user for rectangle 
            length=int(input("Enter Length of Rectangle : "))
            #validating the length of rectangle
            if length<=0:
                print("Length cannot be negative!")
                break
            breadth=int(input("Enter Breadth of Rectangle : "))
            #validating the breadth of rectangle
            if breadth<=0:
                print("Breadth cannot be negative!")
                break
        elif figure_choice==2:
        # ======================================================
        #                      SQUARE 
        # ======================================================
        #taking input from user for square 
            side=int(input("Enter Side of Square : "))
            #validating the side of square
            if side<=0:
                print("Side cannot be negative!")
                break
        elif figure_choice==3:
        # ======================================================
        #                      CIRCLE 
        # ======================================================
        #taking input from user for circle 
            radius=int(input("Enter Radius of Circle : "))
            #validating the radius of circle
            if radius<=0:
                print("Radius cannot be negative!")
                break
        elif figure_choice==4:
        # ======================================================
        #                      TRIANGLE 
        # ======================================================
        #taking input from user for triangle 
            side1=int(input("Enter Side 1 of Triangle : "))
            #validating the side 1 of triangle
            if side1<=0:
                print("Side 1 cannot be negative!")
                break
            side2=int(input("Enter Side 2 of Triangle : "))
            #validating the side 2 of triangle
            if side2<=0:
                print("Side 2 cannot be negative!")
                break
            side3=int(input("Enter Side 3 of Triangle : "))
            #validating the side 3 of triangle
            if side3<=0:
                print("Side 3 cannot be negative!")
                break
            #checking if triangle can be formed
            if side1+side2<=side3 or side1+side3<=side2 or side2+side3<=side1:
                print("Triangle cannot be formed!")
                break
            if side1==side2==side3:
                print("Equilateral Triangle")
            elif side1==side2 or side1==side3 or side2==side3:
                print("Isosceles Triangle")
            else:
                print("Scalene Triangle")
        elif figure_choice==5:
        # ======================================================
        #                      RHOMBUS 
        # ======================================================
        #taking input from user for rhombus 
            diagonal1=int(input("Enter Diagonal 1 of Rhombus : "))
            #validating the diagonal 1 of rhombus
            if diagonal1<=0:
                print("Diagonal 1 cannot be negative!")
                break
            diagonal2=int(input("Enter Diagonal 2 of Rhombus : "))
            #validating the diagonal 2 of rhombus
            if diagonal2<=0:
                print("Diagonal 2 cannot be negative!")
                break
        elif figure_choice==6:
        # ======================================================
        #                      PARALLELOGRAM 
        # ======================================================
        #taking input from user for parallelogram 
            base=int(input("Enter Base of Parallelogram : "))
            #validating the base of parallelogram
            if base<=0:
                print("Base cannot be negative!")
                break
            height=int(input("Enter Height of Parallelogram : "))
            #validating the height of parallelogram
            if height<=0:
                print("Height cannot be negative!")
                break
        elif figure_choice==7:
        # ======================================================
        #                      TRAPEZIUM 
        # ======================================================
        #taking input from user for trapezium 
            base1=int(input("Enter Base 1 of Trapezium : "))
            #validating the base 1 of trapezium
            if base1<=0:
                print("Base 1 cannot be negative!")
                break
            base2=int(input("Enter Base 2 of Trapezium : "))
            #validating the base 2 of trapezium
            if base2<=0:
                print("Base 2 cannot be negative!")
                break
            height=int(input("Enter Height of Trapezium : "))
            #validating the height of trapezium
            if height<=0:
                print("Height cannot be negative!")
                break
        elif figure_choice==8:
        # ======================================================
        #                      KITE 
        # ======================================================
        #taking input from user for kite 
            diagonal1=int(input("Enter Diagonal 1 of Kite : "))
            #validating the diagonal 1 of kite
            if diagonal1<=0:
                print("Diagonal 1 cannot be negative!")
                break
            diagonal2=int(input("Enter Diagonal 2 of Kite : "))
            #validating the diagonal 2 of kite
            if diagonal2<=0:
                print("Diagonal 2 cannot be negative!")
                break
        elif figure_choice==9:
        # ======================================================
        #                      ELLIPSE 
        # ======================================================
        #taking input from user for ellipse 
            major_axis=int(input("Enter Major Axis of Ellipse : "))
            #validating the major axis of ellipse
            if major_axis<=0:
                print("Major Axis cannot be negative!")
                break
            minor_axis=int(input("Enter Minor Axis of Ellipse : "))
            #validating the minor axis of ellipse
            if minor_axis<=0:
                print("Minor Axis cannot be negative!")
                break
        else:
            print("Invalid Choice!")
            break
    #==========================================================
    #                       OPERATION MENU
    #==========================================================
        #menu for selecting operation
        print("\nMenu Operation:")
        print("1. Area")
        print("2. Perimeter")
        #taking input from user for operation
        operation_choice=int(input("Enter your choice (1-2): "))
        #validating the operation choice
        if operation_choice<1 or operation_choice>2:
            print("Invalid Choice!")
            break
        #==========================================================
        #                       CALCULATION
        #==========================================================
        #calculation of area and perimeter for selected figure
        if operation_choice==1:
            if figure_choice==1:
                area=ap.area_rectangle(length,breadth)
                print("Area of Rectangle : ",area)
            elif figure_choice==2:
                area=ap.area_square(side)
                print("Area of Square : ",area)
            elif figure_choice==3:
                area=ap.area_circle(radius)
                print("Area of Circle : ",area)
            elif figure_choice==4:
                if side1==side2==side3:
                    area=ap.area_equilateral_triangle(side1)
                    print("Area of Equilateral Triangle : ",area)
                elif side1==side2 or side1==side3 or side2==side3:
                    area=ap.isosceles_area(side1,side2,side3)
                    print("Area of Isosceles Triangle : ",area)
                else:
                    area=ap.heron_area(side1,side2,side3)
                    print("Area of Scalene Triangle : ",area)
            elif figure_choice==5:
                area=ap.area_rhombus(diagonal1,diagonal2)
                print("Area of Rhombus : ",area)
            elif figure_choice==6:
                area=ap.area_parallelogram(base,height)
                print("Area of Parallelogram : ",area)
            elif figure_choice==7:
                area=ap.area_trapezium(base1,base2,height)
                print("Area of Trapezium : ",area)
            elif figure_choice==8:
                area=ap.area_kite(diagonal1,diagonal2)
                print("Area of Kite : ",area)
            elif figure_choice==9:
                area=ap.area_ellipse(major_axis,minor_axis)
                print("Area of Ellipse : ",area)
        elif operation_choice==2:
            if figure_choice==1:
                perimeter=ap.perimeter_rectangle(length,breadth)
                print("Perimeter of Rectangle : ",perimeter)
            elif figure_choice==2:
                perimeter=ap.perimeter_square(side)
                print("Perimeter of Square : ",perimeter)
            elif figure_choice==3:
                perimeter=ap.perimeter_circle(radius)
                print("Perimeter of Circle : ",perimeter)
            elif figure_choice==4:
                if side1==side2==side3:
                    perimeter=ap.perimeter_equilateral_triangle(side1)
                    print("Perimeter of Equilateral Triangle : ",perimeter)
                elif side1==side2 or side1==side3 or side2==side3:
                    perimeter=ap.isosceles_perimeter(side1,side2,side3)
                    print("Perimeter of Isosceles Triangle : ",perimeter)
                else:
                    perimeter=ap.heron_perimeter(side1,side2,side3)
                    print("Perimeter of Scalene Triangle : ",perimeter)
            elif figure_choice==5:
                perimeter=ap.rhombus_perimeter(diagonal1)
                print("Perimeter of Rhombus : ",perimeter)
            elif figure_choice==6:
                perimeter=ap.parallelogram_perimeter(base,height)
                print("Perimeter of Parallelogram : ",perimeter)
            elif figure_choice==7:
                perimeter=ap.trapezium_perimeter(base1,base2,height)
                print("Perimeter of Trapezium : ",perimeter)
            elif figure_choice==8:
                perimeter=ap.kite_perimeter(diagonal1,diagonal2)
                print("Perimeter of Kite : ",perimeter)
            elif figure_choice==9:
                perimeter=ap.perimeter_ellipse(major_axis,minor_axis)
                print("Perimeter of Ellipse : ",perimeter)
        else:
            print("Invalid Choice!")
            break
        break
    
   