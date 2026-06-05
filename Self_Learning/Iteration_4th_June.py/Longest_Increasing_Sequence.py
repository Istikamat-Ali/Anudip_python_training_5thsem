# 3.> program to find the length of the longest continuous increasing sequence
# The program takes the number of elements and the elements themselves as input, and then finds the length of the longest continuous increasing sequence among the elements.
print("---------------------Longest Continuous Increasing Sequence Finder---------------------")
# input a number using loop not use list concept
N = int(input("Enter the number of elements: "))
# validating the input
if N <= 0:
    exit("Please enter a positive number for the number of elements...Exited")
print("Enter the elements one by one:")
# taking first element as previous element
previous_num = int(input("Enter element 1: ")) 
# validating the input
if previous_num < 0:
    exit("Please enter a positive number for the elements...Exited")
print("-------------------------------------------------------------")
# finding the length of the longest continuous increasing sequence using for loop
longest_length = 1 # initializing longest length to 1 since the minimum length of a sequence is 1
current_length = 1 # initializing current length to 1 since we start with the first element as the previous element

for i in range(1, N):# starting from 1 since we have already taken the first element as input
    num = int(input("Enter element " + str(i + 1) + ": "))# taking input for the current element
    # validating the input
    if num < 0:
        exit("Please enter a positive number for the elements...Exited")
    if num > previous_num:  # comparing current number with previous number
        current_length += 1  # if current number is greater than previous number, increment current_length
    else:
        longest_length = max(longest_length, current_length)  # if current number is not greater than previous number, update longest_length and reset current_length to 1
        current_length = 1
    previous_num = num  # updating previous number
# checking for the last sequence after the loop ends
longest_length = max(longest_length, current_length)
# displaying the result
print("Longest Sequence Length =", longest_length)