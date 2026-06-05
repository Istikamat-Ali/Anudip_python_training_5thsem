'''
Problem Statement
Given a list:
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

Write a program to:
1. Find all pairs of consecutive numbers.
2. Store all consecutive pairs in a new list.

Expected Output:
4 and 5 are consecutive
5 and 6 are consecutive
10 and 11 are consecutive
15 and 16 are consecutive
16 and 17 are consecutive

Additional Challenge:
[(4,5), (5,6), (10,11), (15,16), (16,17)]
'''

print("---------------------- Consecutive Number Detector ----------------------")

# Given list of numbers
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

# ------------------------------------------------------------------------
print("-------------------- Finding Consecutive Numbers -----------------------")
# ------------------------------------------------------------------------

# Create an empty list to store consecutive pairs
consecutive_pairs = []

# Check each number with the next number in the list
for i in range(len(numbers) - 1):

    # If difference between two numbers is 1,
    # then they are consecutive
    if numbers[i + 1] - numbers[i] == 1:

        print(numbers[i], "and", numbers[i + 1], "are consecutive")

        # Store the consecutive pair in the list
        consecutive_pairs.append((numbers[i], numbers[i + 1]))

print("------------------------------------------------------------------------")

# ------------------------------------------------------------------------
print("-------------------- List of Consecutive Pairs -------------------------")
# ------------------------------------------------------------------------

print("Consecutive Pairs:", consecutive_pairs)

print("------------------------------------------------------------------------")