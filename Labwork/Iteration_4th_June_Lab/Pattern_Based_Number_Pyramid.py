# Problem Statement:
# Accept the number of rows and print the following pattern:
# For Input:
# 5
# Output:
# 1
# 12
# 123
# 1234
# 12345
# Challenge:
# Print the reverse pattern as well.
#program to print pattern based number pyramid
print("---------------------Pattern Based Number Pyramid---------------------")
# input number of rows from user
rows = int(input("Enter the number of rows: "))
# validating the input
if rows <= 0:
    exit("Number of rows should be a positive integer ...Exited")
print("-------------------------------------------------------------")
# printing the pattern
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()  # for new line
# printing the reverse pattern
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()  # for new line     
    