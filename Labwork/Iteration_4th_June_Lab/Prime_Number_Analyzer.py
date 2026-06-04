# program to check if a number is prime and to find its factors if it is not prime

# input a number from user
number = int(input("Enter a number: "))

# validating the input
if number < 0:
    exit("Negative numbers are not considered for prime number ...Exited")

print("-------------------------------------------------------------")

# initializing variable to check if the number is prime
is_prime = True

# checking if the number is prime
if number < 2:
    is_prime = False
else:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

# displaying the result
if is_prime:
    print(number, "is a prime number.")
else:
    # finding and displaying all factors of the number
    print("Factors of", number, "are:", end=" ")

    for i in range(1, number + 1):
        if number % i == 0:
            print(i, end=" ")
    print("\n")
    print(number, "is not a prime number.")