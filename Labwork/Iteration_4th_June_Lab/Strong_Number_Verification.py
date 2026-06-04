#A Strong Number is a number whose sum of factorials of digits equals the number itself.
#program to check whether a given number is a Strong Number.
print("---------------------Strong Number Verification---------------------")
# input a number from user
number = int(input("Enter a number: "))
# validating the input
if number < 0:
    exit("Negative numbers cannot be Strong numbers ...Exited")
print("-------------------------------------------------------------")
# storing original number
original_number = number
# initializing sum
sum_of_factorials = 0
# calculating sum of factorials of digits
while number > 0:
    digit = number % 10
    # calculating factorial of digit
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    sum_of_factorials += factorial
    number = number // 10
# checking Strong number condition
if sum_of_factorials == original_number:
    print(original_number, "is a Strong number.")
else:
    print(original_number, "is not a Strong number.")