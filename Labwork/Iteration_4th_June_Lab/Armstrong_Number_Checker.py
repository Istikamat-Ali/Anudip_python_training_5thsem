#program to check if a number is an Armstrong number
print("---------------------Armstrong Number Checker---------------------")
#input a number from user
number = int(input("Enter a number: "))
#validating the input
if number < 0:
    exit("Negative numbers cannot be Armstrong numbers ...Exited")  
print("-------------------------------------------------------------")
# storing original number
original_number = number
# counting digits
num_digits = len(str(number))

# initializing sum
sum_of_powers = 0

# calculating sum of digits raised to power of number of digits
while number > 0:
    digit = number % 10
    sum_of_powers += digit ** num_digits
    number = number // 10

# checking Armstrong condition
if sum_of_powers == original_number:
    print(original_number, "is an Armstrong number.")
else:
    print(original_number, "is not an Armstrong number.")