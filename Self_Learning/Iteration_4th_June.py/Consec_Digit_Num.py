# 1.> program to check if digits of a number are consecutive
print("---------------------Consecutive Digit Number Checker---------------------")
# input a number from user
number = input("Enter a number: ")
# validating the input
if number<0:
    exit("Please enter a positive number...Exited")
print("-------------------------------------------------------------")
# checking if digits are consecutive using for loop
is_consecutive = True
for i in range(1, len(number)):
    if int(number[i]) != int(number[i-1]) + 1: # comparing current digit with previous digit
        is_consecutive = False # marking the number as not consecutive
        break # if any digit is not consecutive, break the loop and set is_consecutive to False
# displaying the result
if is_consecutive:
    print("Consecutive Number")
else:   
    print("Not a Consecutive Number")
