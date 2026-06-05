# 7.> program to check if a number is a Mirror Number
# Mirror number is a number whose left half is identical to the right half
print("---------------------Mirror Number Checker---------------------")
# input a number from user
number = input("Enter a number: ")
# validating the input
if number<0:
    exit("Please enter a positive number...Exited")
print("-------------------------------------------------------------")
# checking if left half of the number is identical to the right half
length = len(number)# getting the length of the number to determine the halves
if length % 2 != 0:# checking if the number has an even number of digits
    exit("Number must have an even number of digits...Exited")
left_half = number[:length//2] # getting the left half of the number
right_half = number[length//2:] # getting the right half of the number
if left_half == right_half:
    print("Mirror Number")
else:   
    print("Not a Mirror Number")    