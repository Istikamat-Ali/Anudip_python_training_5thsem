'''Problem Statement 1: File Content Analyzer
A publishing company maintains articles in text files and wants to generate basic statistics about the content 
stored in these files. As a software developer, you have been assigned the task of creating a program that 
reads the contents of a text file and analyzes the information present in it.
Requirements
Write a Python program that reads data from a text file and displays the following details:
1. Total number of vowels present in the file. 
2. Total number of characters present in the file (including spaces and special characters). 
3. Total number of lines present in the file. 
Sample File Content (article.txt)
Python is an easy-to-learn programming language.
It supports multiple programming paradigms.
File handling allows programs to work with data stored in files.
Expected Output
File Analysis Report
Total Number of Vowels : 42
Total Number of Characters: 153
Total Number of Lines : 3'''
print("---------------------File Content Analyzer---------------------")
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