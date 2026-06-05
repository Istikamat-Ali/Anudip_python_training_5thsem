#8.> program to count minimum number of notes required for a given amount
print("---------------------Coin Change Counter---------------------")
# input amount from user
amount = int(input("Enter the amount: "))
# validating the input
if amount < 0:
    exit("Please enter a positive amount...Exited")
print("-------------------------------------------------------------")
# list of available notes in descending order
notes = [500, 200, 100, 50, 20, 10]
# counting the number of notes required for each denomination
for note in notes:
    count = amount // note # calculating how many notes of the current denomination are needed
    if count > 0: # if at least one note of the current denomination is needed
        print(note,"x",count) # displaying the denomination and count
        amount -= note * count # reducing the remaining amount by the total value of the notes counted 
        
        
        
        
        
        
 
        