#program to make a simple calculator
#input of first number
num1=float(input("Enter the first number: "))
#input of second number
num2=float(input("Enter the second number: "))
#input of operator
operator=input("Enter the operator (+, -, *, /): ")
#check operator and perform corresponding operation
if(operator=="+"):
    result=num1+num2
    print("The sum of ", num1, "and", num2, "is: ", result)
elif(operator=="-"):
    result=num1-num2
    print("The difference of ", num1, "and", num2, "is: ", result)
elif(operator=="*"):
    result=num1*num2
    print("The product of ", num1, "and", num2, "is: ", result)
elif(operator=="/"):
    if(num2==0):
        print("Division by zero is not allowed")
    else:
        result=num1/num2
        print("The quotient of ", num1, "and", num2, "is: ", result)
else:
    print("Invalid operator ... Exited")