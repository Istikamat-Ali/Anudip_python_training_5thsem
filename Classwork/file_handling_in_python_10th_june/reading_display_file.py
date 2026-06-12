'''Problem Statement: To read the data from file and display the following:
1. No. of Vowels in file.
2. No. of characters into the file.
3. No. of lines into the file.'''
#reading file
with open("article.txt", "r") as file:
    content = file.read()
    print("File Analysis Report")
    count_vowels = 0
    #counting vowels
    for char in content:
        if char in "aeiouAEIOU":
            count_vowels+=1
    print("Total Number of Vowels:",count_vowels)
    print("Total Number of Characters:", len(content))
    print("Total Number of Lines:", content.count("\n"))
print("---------------------------------------------------------------------------------")