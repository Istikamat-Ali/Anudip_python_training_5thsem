# 2.> program to check if a number is a Mountain Number
#Mountain number is a number whose digits first increase and then decrease
print("---------------------Mountain Number Checker---------------------")
# input a number from user
number = input("Enter a number: ")
# validating the input
if int(number) < 0 or not number.isdigit():
    exit("Please enter a valid number...Exited")
print("-------------------------------------------------------------")
# checking if digits are in increasing order using for loop
is_increasing = True
for i in range(1, len(number)):
    if int(number[i]) <= int(number[i-1]): # comparing current digit with previous digit
        is_increasing = False # marking the number as not increasing
        break # if any digit is not increasing, break the loop and set is_increasing to False
# checking if digits are in decreasing order using for loop
is_decreasing = True
for i in range(1, len(number)):
    if int(number[i]) >= int(number[i-1]): # comparing current digit with previous digit
        is_decreasing = False # marking the number as not decreasing
        break # if any digit is not decreasing, break the loop and set is_decreasing to False
# displaying the result
if is_increasing and is_decreasing:
    print("Mountain Number")
else:   
    print("Not a Mountain Number")